<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

---

<!-- PROJECT LOGO -->

[![Logo](/images/mark-matheson-digital-business-consultant.png)](../../)

# Matho's Home Assistant Configuration

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![HA Version][ha-version-shield]][home-assistant]
[![GitHub Sponsor Me][github-sponsor-me-shield]][github-sponsors-url]
<a href="https://www.buymeacoffee.com/nzrunner" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="28" width="174"></a><br />
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Bugs][bugs-shield]][bugs-url]
[![Feature Requests][features-shield]][features-url]
[![Pull Requests][pull-request-shield]][pull-request-url]
[![MIT License][license-shield]][license-url]
[![GitHub Sponsors][github-sponsors-shield]][github-sponsors-url]<br />
[![Project Maintenance][maintenance-shield]](https://github.com/nzrunner/home-assistant/pulse)
[![GitHub Activity][commits-shield]][commits]
[![GitHub Last Commit][last-commit-shield]][commits]
[![Home Assistant CI][homeassistantci-shield]][homeassistantci]

---

<!-- PROJECT SHORT DESCRIPTION AND MENU -->

[🏡 Home](https://github.com/nzrunner/home-assistant)
|
[📚 Git Guide](/docs/git-guide.md)
|
[💻 Resources](/docs/resources.md)
|
[🐛 Report Bug](https://github.com/nzrunner/home-assistant/issues/new?assignees=nzrunner&labels=%F0%9F%90%9B+Bug%2C%F0%9F%A9%B9+Triage&template=bug_report.yml&title=%5BBUG%5D%3A+)
|
[👍 Request Feature](https://github.com/nzrunner/home-assistant/issues/new?assignees=nzrunner&labels=%F0%9F%91%8D+Enhancement%2C%F0%9F%A9%B9+Triage&template=feature_request.yml&title=%5BFEATURE+REQUEST%5D%3A+)
|
[🗒 ChangeLog](/CHANGELOG.md)

<!-- TABLE OF CONTENTS -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [Overview](#overview)
  - [Updates](#updates)
  - [Update: 2023-04-25](#update-2023-04-25)
- [Built With](#built-with)
- [Dashboards](#dashboards)
  - [Screenshots](#screenshots)
  - [Lovelace UI](#lovelace-ui)
- [Integrations](#integrations)
- [Custom Components](#custom-components)
  - [Integrations](#integrations-1)
  - [Frontend](#frontend)
  - [Automation](#automation)
  - [Addons](#addons)
- [Devices](#devices)
  - [Network](#network)
  - [IOT](#iot)
- [Roadmap](#roadmap)
- [Acknowledgments](#acknowledgments)
  - [Themes](#themes)
  - [Inspiration](#inspiration)
- [Contributing](#contributing)
  - [Our Contributors](#our-contributors)
- [Sponsorship](#sponsorship)
  - [Our Sponsors](#our-sponsors)
- [License](#license)
- [Contact](#contact)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

---

<!-- ABOUT THE PROJECT -->

## Overview

[Home Assistant](https://home-assistant.io) is an awesome open-source home automation product that I have deployed to run my house.

I created this project to: -

- Document my configuration (always a good thing)
- Have a backup of my configuration (another good thing)
- Contribute to the open-source community
- Learn GitHub

As I continue to make improvements to my smart home, I will be updating my configuration. Be sure to ⭐ my page and stay tuned for the latest updates.

Hopefully, as I have learned from others and "borrowed" sectons of their code, others can benefit from my configuration.

Sadly, I didn't keep a good record of the initial Home Assistant configurations that inspired me. If I stumble over them again, I will add them to the [Acknowledgements](#acknowledgments) section.

### Updates

<details>
<summary>Update: 2023-04-26</summary>

### Update: 2023-04-26

I spent some time trying to get Home Assistant Voice working. I found it to be an extremely frustrating experience. The documentation while comprehensive, is confusing and disjointed. Just my humble opinion.

I am pleased to say, I have it working within the app, albeit only in a browser on my laptop and not in the app on my mobile devices. I suspect this is related to my http intergration, despite the fact both my internal and external URL's are using https.

_Note: Finally stumbled on the Apple iPhone Shortcuts that I needed to make it work on my mobile devices, and "Hey Siri, Assist" is working nicely but still no joy getting voice working from within the mobile app._

For my conversation integration, the two files I needed to create were [includes/intent_script.yaml][/includes/intent_script.yaml] and [custom_sentences/en/domestic.yaml][custom_sentences/en/domestic.yaml]. The later file can be named anything, but must be in the custom_sentences/{language} folder.

Although I have several Google Home devices, I am not comfortable with the Google servers being "fed" all the data relating to my devices, so won't be adding the Google Home integration at this point. Besides, it's a lot of work for little benefit.

So, guess it's back to talking to myself again when I want my smart home to do something. <ponders>

</details>

<details>
<summary>Update: 2023-04-25</summary>

### Update: 2023-04-25

Exploring other people's Git repositories led me to investing time in learning about GitHub actions. All I can say is wow! My programming skills are OK at best, but learning from others in the open-source community has resulted in me now having some awesome CI workflows running on my Git repository, making life so much easier. In addition, I learnt about Git pre-commit hooks, and have a few of these running on my RPi, meaning the code I upload is much cleaner.

I have adopted a similar approach to @frenck and @metbril and have enhanced how my configuration file is split up. It was difficult to understand at first, but once I understood the structure, it made perfect sense. For anyone even mildly interested, it is definitely worth investing the time and effort. Links to their configurations are available in the [Acknowledgements](#acknowledgments) section below.

As a result of these major changes in my Git repository, my Home Assistant configuration is cleaner and much easier to understand.

A huge 🙏 thank you to the open-source community!

</details>

## Built With

[![Home Assistant][hass.io]][home-assistant] [![Raspberry Pi][raspberry-pi]](https://www.raspberrypi.com) [![Debian](https://img.shields.io/badge/Debian-AB1D33?style=for-the-badge&logo=debian&logoColor=ffffff)](https://www.debian.org)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Dashboards

### Screenshots

|                             **Preferred Theme**                              |                             **Alternate Theme**                              |
| :--------------------------------------------------------------------------: | :--------------------------------------------------------------------------: |
|       ![Home Assistant](images/home-assistant-preferred.png?raw=true)        |       ![Home Assistant](images/home-assistant-alternate.png?raw=true)        |
|        ![Alerts](images/home-assistant-alerts-preferred.png?raw=true)        |        ![Alerts](images/home-assistant-alerts-alternate.png?raw=true)        |
|        ![System](images/home-assistant-system-preferred.png?raw=true)        |        ![System](images/home-assistant-system-alternate.png?raw=true)        |
|       ![Network](images/home-assistant-network-preferred.png?raw=true)       |       ![Network](images/home-assistant-network-alternate.png?raw=true)       |
|      ![Security](images/home-assistant-security-preferred.png?raw=true)      |      ![Security](images/home-assistant-security-alternate.png?raw=true)      |
| ![Entertainment](images/home-assistant-entertainment-preferred.png?raw=true) | ![Entertainment](images/home-assistant-entertainment-alternate.png?raw=true) |
|     ![Debugging](images/home-assistant-debugging-preferred.png?raw=true)     |     ![Debugging](images/home-assistant-debugging-alternate.png?raw=true)     |
|   ![Docker Server](images/home-assistant-docker-1-preferred.png?raw=true)    |   ![Docker Server](images/home-assistant-docker-1-alternate.png?raw=true)    |
| ![Docker Containers](images/home-assistant-docker-2-preferred.png?raw=true)  | ![Docker Containers](images/home-assistant-docker-2-alternate.png?raw=true)  |

### Lovelace UI

I have opted to maintain my Dashboards using the Home Assistant UI (.storage mode). As such, I don't have a ui-lovalace.yml file accessible in my config folder.

In the interests of completeness, I have copied the YAML code from the Raw Dashboard editor into a YAML file. It can be found [here](/.stubs/lovelace-ui.yaml). _Last update: 24/03/2023_.

I will endeavour to update this occassionally.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Integrations

| **Integration**                    | **Repository**                                               |
| :--------------------------------- | :----------------------------------------------------------- |
| Apple iCloud                       | <https://www.home-assistant.io/integrations/icloud>          |
| Apple TV                           | <https://www.home-assistant.io/integrations/apple_tv>        |
| Brother Printer                    | <https://www.home-assistant.io/integrations/brother>         |
| Sony Bravia TV                     | <https://www.home-assistant.io/integrations/dlna_dmr>        |
| HD HomeRun DMS                     | <https://www.home-assistant.io/integrations/dlna_dms>        |
| My IP                              | <https://www.home-assistant.io/integrations/dnsip>           |
| Google Cast                        | <https://www.home-assistant.io/integrations/cast>            |
| Home Assistant Supervisor          | <https://www.home-assistant.io/integrations/hassio>          |
| HomeKit                            | <https://www.home-assistant.io/integrations/homekit>         |
| Local IP                           | <https://www.home-assistant.io/integrations/local_ip>        |
| Mobile App                         | <https://www.home-assistant.io/integrations/mobile_app>      |
| Philips Hue                        | <https://www.home-assistant.io/integrations/hue>             |
| Pi-Hole                            | <https://www.home-assistant.io/integrations/pi_hole>         |
| Plex Media Server                  | <https://www.home-assistant.io/integrations/pi_hole>         |
| Radarr                             | <https://www.home-assistant.io/integrations/radarr>          |
| SABnzbd                            | <https://www.home-assistant.io/integrations/sabnzbd>         |
| Season                             | <https://www.home-assistant.io/integrations/season>          |
| Sonarr                             | <https://www.home-assistant.io/integrations/sonarr>          |
| Sonos                              | <https://www.home-assistant.io/integrations/sonos>           |
| SpeedTest                          | <https://www.home-assistant.io/integrations/speedtestdotnet> |
| Sun                                | <https://www.home-assistant.io/integrations/sun>             |
| Synology DSM                       | <https://www.home-assistant.io/integrations/synology_dsm>    |
| Tautulli                           | <https://www.home-assistant.io/integrations/tautulli>        |
| TP-Link Kasa Smart                 | <https://www.home-assistant.io/integrations/tplink>          |
| Unifi Network                      | <https://www.home-assistant.io/integrations/unifi>           |
| Uptime                             | <https://www.home-assistant.io/integrations/uptime>          |
| CONBEE II (Zigbee Home Automation) | <https://www.home-assistant.io/integrations/zha>             |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Custom Components

### Integrations

| **Custom Component**     | **Repository**                                                      |
| :----------------------- | :------------------------------------------------------------------ |
| HACS                     | <https://github.com/hacs/integration>                               |
| Unifi Gateway            | <https://github.com/custom-components/sensor.unifigateway>          |
| Auto Backup              | <https://github.com/jcwillox/hass-auto-backup>                      |
| Local Tuya               | <https://github.com/rospogrigio/localtuya>                          |
| Font Awesome             | <https://github.com/thomasloven/hass-fontawesome>                   |
| Browser Mod              | <https://github.com/thomasloven/hass-browser_mod>                   |
| Monitor Docker           | <https://github.com/ualex73/monitor_docker>                         |
| Simple Icons             | <https://github.com/vigonotion/hass-simpleicons>                    |
| Garbage Collection       | <https://github.com/bruxy70/Garbage-Collection>                     |
| Radarr Upcoming Media    | <https://github.com/custom-components/sensor.radarr_upcoming_media> |
| Sonarr Upcoming Media    | <https://github.com/custom-components/sensor.sonarr_upcoming_media> |
| Lidarr Upcoming Media    | <https://github.com/JackJPowell/sensor.lidarr_upcoming_media>       |
| Bereau of Meteorology    | <https://github.com/bremor/bureau_of_meteorology>                   |
| Plex Recently Added      | <https://github.com/custom-components/sensor.plex_recently_added>   |
| Average Sensor           | <https://github.com/Limych/ha-average>                              |
| Garmin Conenct           | <https://github.com/cyberjunky/home-assistant-garmin_connect>       |
| ICS Calendar (iCalendar) | <https://github.com/franc6/ics_calendar>                            |
| Uptime Kuma              | <https://github.com/meichthys/uptime_kuma>                          |
| Medisafe                 | <https://github.com/c99koder/ha-medisafe>                           |

### Frontend

| **Custom Component**                  | **Repository**                                              | **Notes**                        |
| :------------------------------------ | :---------------------------------------------------------- | :------------------------------- |
| Multiple Entity Row                   | <https://github.com/benct/lovelace-multiple-entity-row>     |
| Bar Card                              | <https://github.com/custom-cards/bar-card>                  |
| Button Card                           | <https://github.com/custom-cards/button-card>               | Major Use                        |
| Decluttering Card                     | <https://github.com/custom-cards/decluttering-card>         | Not currently used               |
| ZHA Network Card                      | <https://github.com/dmulcahey/zha-network-card>             |
| Mini Media Player                     | <https://github.com/kalkih/mini-media-player>               |
| Auto Entities                         | <https://github.com/thomasloven/lovelace-auto-entities>     |
| Card Mod                              | <https://github.com/thomasloven/lovelace-card-mod>          |
| Fold Entity Row                       | <https://github.com/thomasloven/lovelace-fold-entity-row>   |
| Slider Entity Row                     | <https://github.com/thomasloven/lovelace-slider-entity-row> |
| IOS Themes - Dark Mode and Light Mode | <https://github.com/basnijholt/lovelace-ios-themes>         | My primary theme                 |
| Custom Brand Icons                    | <https://github.com/elax46/custom-brand-icons>              |
| Digital Clock                         | <https://github.com/wassy92x/lovelace-digital-clock>        |
| Custom Animated Weather Card          | <https://github.com/DavidFW1960/bom-weather-card>           | Swapped to Platinum Weather Card |
| Battery State Card                    | <https://github.com/maxwroc/battery-state-card>             |
| Mini Graph Card                       | <https://github.com/kalkih/mini-graph-card>                 |
| Upcoming Media Card                   | <https://github.com/custom-cards/upcoming-media-card>       |
| Layout Card                           | <https://github.com/thomasloven/lovelace-layout-card>       |
| Hass Hue Icons                        | <https://github.com/arallsopp/hass-hue-icons>               |
| Metrology - Metro and Fluent Themese  | <https://github.com/Madelena/Metrology-for-Hass>            | My alternate theme               |
| Platinum Weather Card                 | <https://github.com/Makin-Things/platinum-weather-card>     |

### Automation

| **Automation** | **Repository**                            |
| :------------- | :---------------------------------------- |
| Config Check   | <https://github.com/apop880/config-check> |

### Addons

| **Addon**        | **Repository**                                                    |
| :--------------- | :---------------------------------------------------------------- |
| AppDaemon        | <https://github.com/hassio-addons/addon-appdaemon>                |
| VS Code          | <https://github.com/hassio-addons/addon-vscode>                   |
| Terminal and SSH | <https://github.com/home-assistant/hassio-addons/tree/master/ssh> |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Devices

### Network

| **Equipment**                  | **Website**                                                  |
| :----------------------------- | :----------------------------------------------------------- |
| Ubiquiti Unifi USG 3 Router    | <https://ui.com/consoles>                                    |
| Ubiquiti Unifi AP Lite         | <https://ui.com/wi-fi>                                       |
| Ubiquiti Unifi Switches        | <https://ui.com/switching>                                   |
| Ubiquiti Unifi Cloud Key GEN 1 | <https://ui.com/consoles>                                    |
| Brother L8250CDN Printer       | No longer available                                          |
| Synology DS1812+ NAS           | No longer available                                          |
| Synology DS1618+ NAS           | No longer available                                          |
| Sonos One Speakers             | <https://www.sonos.com/en-au/shop/one-sl>                    |
| Google Home Mini Speakers      | <https://store.google.com/product/google_nest_mini?hl=en-AU> |
| Apple iPhone                   | <https://www.apple.com/au/iphone/>                           |
| Apple iPad                     | <https://www.apple.com/au/ipad/>                             |

### IOT

| **Equipment**                  | **Number** | **Website**                                                                                                          | **Notes** |
| :----------------------------- | :--------: | :------------------------------------------------------------------------------------------------------------------- | :-------- |
| Aqara Motion Sensors           |     8      | <https://www.aqara.com/en/human_motion_sensor.html>                                                                  |
| Aqara Door Sensors             |     8      | <https://www.aqara.com/en/door_and_window_sensor.html>                                                               |
| Aqara Temperature Sensors      |     4      | <https://www.aqara.com/en/temperature_humidity_sensor.html>                                                          |
| Aqara Mini Switch              |     1      | <https://www.aqara.com/en/smart_wireless_mini_switch.html>                                                           |
| Aqara Blind Controller         |     1      | <https://www.aqara.com/en/product/roller-shade-driver-e1>                                                            |
| Philips Hue Bridge             |     1      | <https://www.philips-hue.com/en-au/p/hue-bridge/8719514342569>                                                       |
| Philips Hue Smart Bulbs        |     13     | <https://www.philips-hue.com/en-au/products/smart-light-bulbs>                                                       |
| Philips Hue Light Strips       |     1      | <https://www.philips-hue.com/en-au/products/smart-light-strips>                                                      |
| Philips Hue Motion Sensors     |     2      | <https://www.philips-hue.com/en-au/p/hue-motion-sensor/8719514342149>                                                |
| Philips Hue Dimmer Switch      |     1      | <https://www.philips-hue.com/en-au/p/hue-dimmer-switch--latest-model-/8719514274631>                                 |
| IKEA Tradfri Motion Sensors    |     2      | <https://www.ikea.com/au/en/p/tradfri-wireless-motion-sensor-smart-white-90370469/>                                  |
| IKEA Tradfri Buttons           |     2      | <https://www.ikea.com/au/en/p/tradfri-shortcut-button-white-smart-80356384/>                                         |
| IKEA Tradfri Smart Bulbs       |     2      | <https://www.ikea.com/au/en/p/tradfri-led-bulb-e14-470-lumen-smart-wireless-dimmable-white-spectrum-globe-20489730/> |
| IKIEA Tradfri Signal repeater  |     1      | <https://www.ikea.com/au/en/p/tradfri-signal-repeater-30400412/>                                                     |
| Arlec Smart Plugs              |     8      | <https://www.bunnings.com.au/arlec-grid-connect-smart-plug-in-socket-with-energy-meter-4-pack_p0273368>              |
| TP-Link HS110 Smart Plug       |     1      | <https://www.tp-link.com/au/home-networking/smart-plug/hs110/>                                                       |
| TP-Link KP303 Smart Powerboard |     1      | <https://www.tp-link.com/au/home-networking/smart-plug/kp303/>                                                       | Garbage   |
| Security Cameras               |     2      | N/A                                                                                                                  |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

<details>

<summary>Roadmap completed</summary>

- [x] Review project files for items that should be in the secrets.yaml file
- [x] Disable Bluetooth Tracker
- [x] Update the README
  - [x] Complete Integrations list (with links)
  - [x] Complete Custom Components section (with links)
  - [x] Improve the content in the About The Project section
  - [x] Update the Roadmap section
  - [x] Add a Devices section (with links)
    - [x] IoT devices
    - [x] Other devices
  - [x] Update Built-With section, describing the hardware and OS configuration
- [x] Logo
  - [x] Use a file stored in the project
  - [x] Design a project specific image (Canva)
- [x] Add Roadmap items as Feature Requests in the Issues list
- [x] Add a Change Log
- [x] Redo screenshots with preferred theme colour
- [x] Write a Git Guide
- [x] Adopt a git commit message convention
- [x] Publish the lovelace-ui.yaml
- [x] Publish fake secrets.yaml for completeness

</details>

See the [open issues](https://github.com/nzrunner/home-assistant/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

### Themes

| **Description**                         | **Link**                                             |
| :-------------------------------------- | :--------------------------------------------------- |
| My primary theme - iOS Themes           | <https://github.com/basnijholt/lovelace-ios-themes/> |
| My alternate theme - Metrology (Fluent) | <https://github.com/Madelena/Metrology-for-Hass>     |

### Inspiration

| **Description**                                | **Link**                                              |
| :--------------------------------------------- | :---------------------------------------------------- |
| My inspiration - @frenck's configuration       | <https://github.com/frenck/home-assistant-config>     |
| More inspiration - @Metbril's configuration    | <https://github.com/metbril/home-assistant-config>    |
| Well documented - @basnijholt's configuration  | <https://github.com/basnijholt/home-assistant-config> |
| Also well documented - @pqpxo configuration    | <https://github.com/pqpxo/SWAKES_hassio>              |
| Amazing documentation - @CCOSTAN configuration | <https://github.com/CCOSTAN/Home-AssistantConfig>     |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Thank you for investing your time in contributing to our project! Any contribution you make will be reflected on [https://github.com/nzrunner/home-assistant](https://github.com/nzrunner/home-assistant) :sparkles:.

Read our [Code of Conduct](./.github/CODE_OF_CONDUCT.md) to keep our community approachable and respectable.

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Our Contributors

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/nzrunner">
            <img src="https://avatars.githubusercontent.com/u/5681652?v=4" width="100;" alt="nzrunner"/>
            <br />
            <sub><b>Mark Matheson</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SPONSORSHIP -->

## Sponsorship

If you like what I've done, please consider sponsoring me. Like everyone, I have costs associated with maintaining this repository. Any little bit will help.

[![GitHub Sponsor Me][github-sponsor-me-shield]][github-sponsors-url]
<a href="https://www.buymeacoffee.com/nzrunner" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="28" width="174"></a>

### Our Sponsors

<!-- readme: nzrunner,sponsors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/nzrunner">
            <img src="https://avatars.githubusercontent.com/u/5681652?v=4" width="100;" alt="nzrunner"/>
            <br />
            <sub><b>Mark Matheson</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: nzrunner,sponsors -end -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See [LICENSE.md](./LICENSE.md) for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

| **Name**      | **Handle** | **Link**                                     |
| :------------ | :--------- | :------------------------------------------- |
| Mark Matheson | @nzrunner  | <https://twitter.com/nzrunner>               |
| Project Link  |            | <https://github.com/nzrunner/home-assistant> |

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- Shields -->

[contributors-shield]: https://img.shields.io/github/contributors/nzrunner/home-assistant.svg?style=flat-square
[forks-shield]: https://img.shields.io/github/forks/nzrunner/home-assistant.svg?style=flat-square
[stars-shield]: https://img.shields.io/github/stars/nzrunner/home-assistant.svg?style=flat-square
[bugs-shield]: https://img.shields.io/github/issues-search/nzrunner/home-assistant?style=flat-square&label=Bugs&query=is%3Aopen%20is%3Aissue%20label%3Abug
[features-shield]: https://img.shields.io/github/issues-search/nzrunner/home-assistant?style=flat-square&label=Feature%20Requests&query=is%3Aopen%20is%3Aissue%20label%3Aenhancement
[license-shield]: https://img.shields.io/github/license/nzrunner/home-assistant.svg?style=flat-square
[commits-shield]: https://img.shields.io/github/commit-activity/y/nzrunner/home-assistant.svg?style=flat-square
[maintenance-shield]: https://img.shields.io/maintenance/yes/2023.svg?style=flat-square
[last-commit-shield]: https://img.shields.io/github/last-commit/nzrunner/home-assistant.svg?style=flat-square
[hass.io]: https://img.shields.io/badge/Home%20Assistant-blue?style=for-the-badge&logo=home-assistant&logoColor=#41BDF5
[raspberry-pi]: https://img.shields.io/badge/Raspberry%20Pi-A22846?style=for-the-badge&logo=raspberry-pi&logoColor=ffffff
[homeassistantci-shield]: https://img.shields.io/github/actions/workflow/status/nzrunner/home-assistant/home_assistant.yml?label=Home%20Assistant%20CI&style=flat-square
[ha-version-shield]: https://img.shields.io/badge/Home%20Assistant-2023.3-blue.svg?style=for-the-badge
[github-sponsors-shield]: https://img.shields.io/github/sponsors/nzrunner?label=Sponsors&style=flat-square
[github-sponsor-me-shield]: https://img.shields.io/badge/sponsor-lightgrey?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#white
[pull-request-shield]: https://img.shields.io/github/issues-pr-raw/nzrunner/home-assistant?label=Pull%20Requests&style=flat-square

<!-- URL's -->

[contributors-url]: https://github.com/nzrunner/home-assistant/graphs/contributors
[forks-url]: https://github.com/nzrunner/home-assistant/network/members
[stars-url]: https://github.com/nzrunner/home-assistant/stargazers
[bugs-url]: https://github.com/nzrunner/home-assistant/issues?q=is%3Aopen+is%3Aissue+label%3A%22%F0%9F%90%9B+Bug%22
[features-url]: https://github.com/nzrunner/home-assistant/issues?q=is%3Aopen+is%3Aissue+label%3A%22%F0%9F%91%8D+Enhancement%22
[license-url]: https://github.com/nzrunner/home-assistant/blob/master/LICENSE.md
[commits]: https://github.com/nzrunner/home-assistant/commits/master
[homeassistantci]: https://github.com/nzrunner/home-assistant/actions/workflows/home_assistant.yml
[home-assistant]: https://home-assistant.io
[github-sponsors-url]: https://github.com/sponsors/nzrunner
[pull-request-url]: https://github.com/nzrunner/home-assistant/pulls
