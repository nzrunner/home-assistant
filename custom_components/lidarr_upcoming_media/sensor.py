"""
Home Assistant component to feed the Upcoming Media Lovelace card with
Lidarr upcoming releases.
https://github.com/custom-cards/upcoming-media-card
"""
import logging
import json
import time
import requests
from datetime import date, datetime
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_API_KEY, CONF_HOST, CONF_PORT, CONF_SSL
from homeassistant.helpers.entity import Entity

__version__ = '0.1'

_LOGGER = logging.getLogger(__name__)

CONF_DAYS = 'days'
CONF_URLBASE = 'urlbase'
CONF_MAX = 'max'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_API_KEY): cv.string,
    vol.Optional(CONF_DAYS, default='7'): cv.string,
    vol.Optional(CONF_HOST, default='localhost'): cv.string,
    vol.Optional(CONF_PORT, default=8686): cv.port,
    vol.Optional(CONF_SSL, default=False): cv.boolean,
    vol.Optional(CONF_URLBASE, default=''): cv.string,
    vol.Optional(CONF_MAX, default=5): cv.string,
})


def setup_platform(hass, config, add_devices, discovery_info=None):
    add_devices([LidarrUpcomingMediaSensor(hass, config)], True)


class LidarrUpcomingMediaSensor(Entity):

    def __init__(self, hass, conf):
        from pytz import timezone
        self.host = conf.get(CONF_HOST)
        self.port = conf.get(CONF_PORT)
        self.urlbase = conf.get(CONF_URLBASE)
        if self.urlbase:
            self.urlbase = "{}/".format(self.urlbase.strip('/'))
        self.apikey = conf.get(CONF_API_KEY)
        self.days = int(conf.get(CONF_DAYS))
        self.ssl = 's' if conf.get(CONF_SSL) else ''
        self._state = None
        self.data = []
        self._tz = timezone(str(hass.config.time_zone))
        self.max_items = int(conf.get(CONF_MAX))

    @property
    def name(self):
        return 'Lidarr_Upcoming_Media'

    @property
    def state(self):
        return self._state

    @property
    def device_state_attributes(self):
        import re
        """Return JSON for the sensor."""
        attributes = {}
        default = {}
        card_json = []
        default['title_default'] = '$title'
        default['line1_default'] = '$studio'
        default['line2_default'] = '$release'
        default['line3_default'] = '$genres'
        default['line4_default'] = '$runtime'
        default['icon'] = 'mdi:music'
        card_json.append(default)
        for album in self.data:
            card_item = {}
            if 'title' not in album:
                continue
            card_item['airdate'] = album['releaseDate']
            if days_until(album['releaseDate'], self._tz) <= 7:
                card_item['release'] = '$day, $time'
            else:
                card_item['release'] = '$day, $date $time'
            
            card_item['studio'] = album['artist']['artistName']
            card_item['title'] = album['title']
            card_item['runtime'] = album['duration'] / 1000 / 60

            if 'genres' in album['genres']:
                card_item['genres'] = ', '.join(album['genres'])
            else:
                card_item['genres'] = ''
            try:
                for img in album['images']:
                    if img['coverType'] == 'cover':
                        card_item['poster'] = re.sub('.jpg', '-250.jpg', 'http{0}://{1}:{2}'.format(self.ssl, self.host, self.port) + img['url'])
                        card_item['fanart'] = re.sub('.jpg', '-250.jpg', 'http{0}://{1}:{2}'.format(self.ssl, self.host, self.port) + img['url'])
            except:
                continue

            card_json.append(card_item)
        attributes['data'] = card_json
        return attributes

    def update(self):
        start = get_date(self._tz)
        end = get_date(self._tz, self.days)
        try:
            api = requests.get('http{0}://{1}:{2}/{3}api/v1/calendar?start={4}'
                                '&end={5}'.format(self.ssl, self.host,
                                                    self.port, self.urlbase,
                                                    start, end),
                                headers={'X-Api-Key': self.apikey}, timeout=10)
        except OSError:
            _LOGGER.warning("Host %s is not available", self.host)
            self._state = '%s cannot be reached' % self.host
            return

        if api.status_code == 200:
            self._state = 'Online'
            if self.days == 1:
                self.data = list(filter(lambda x: x['airDate'][:-10] == str(
                    start), api.json()))[:self.max_items]
            else:
                self.data = api.json()[:self.max_items]
        else:
            self._state = '%s cannot be reached' % self.host


def get_date(zone, offset=0):
    """Get date based on timezone and offset of days."""
    return datetime.date(datetime.fromtimestamp(
        time.time() + 86400 * offset, tz=zone))


def days_until(date, tz):
    from pytz import utc
    date = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    date = str(date.replace(tzinfo=utc).astimezone(tz))[:10]
    date = time.strptime(date, '%Y-%m-%d')
    date = time.mktime(date)
    now = datetime.now().strftime('%Y-%m-%d')
    now = time.strptime(now, '%Y-%m-%d')
    now = time.mktime(now)
    return int((date - now) / 86400)