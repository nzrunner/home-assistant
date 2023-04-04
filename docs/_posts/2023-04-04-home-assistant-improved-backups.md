---
title: Home Assistant ... Improved Backups
layout: post
excerpt_separator: "<!--more-->"
date: "2023-04-04 12:33:00 +1100"
categories:
  - home-assistant
tags:
  - home-assistant
  - backups
  - dropbox
author: mark
header_image: "assets/images/home-assistant-improved-backups.png"
---

After last week's disaster when I almost lost all my Home Assistant configuration, I felt it was time to improve my backup process to ensure I had some offsite backups in case of a genuine disaster occuring.

<!--more-->

# Components

I have been using the [Auto-Backup](https://github.com/jcwillox/hass-auto-backup) integration for some time. It saved my bacon when I deleted key files from my Home Assistant configuration. However, these snapshots are all stored locally and I felt I needed better coverage in case of an incident that rendered my local machine totally inacecssible.

I researched and tried a couple of addons that supposedly enabled syncing these backups to Dropbox. I finally settled on [Dropback](https://github.com/matthewhadley/homeassistant-dropback). This is an addon that worked first time and included very clear documentation.

# Process

The process is very simple. The automation runs and initialises a Home Assistant backup (AKA snapshot). Upon completion, the `sensor.auto_backup_template` changes from `on` to `off` and Dropback kicks in and uploads the snapshot to Dropbox. No manual effort required.

# Automations

I have three automations in place that complete the Auto-Backups. These include: -

- Backup - Midday (Runs at midday every day, retained for 3 days)
- Backup - Midnight (Runs at midnight every day, retained for 6 days)
- Backup - Weekly (Runs at midnight Sunday, retained for 29 days)

These are very similar in their functionality. The key differences are the names I give each backup, the retention period and the times at which they run.

This generational backup scheme ends up giving me 13 backups, ranging from 6 half-daily backups, 3 daily backups and 4 weekly backups.

Each of the backups include the necessary trigger and service call to initiate Dropback. This is designed to only upload snapshots not already found in Dropbox and also mirror the deletion of local snapshots.

_**Note:** The double braces (`{ {` and `} }`) in the code snippets below have a space between them to avoid a Jekyll Liquid syntax error_

## Midday

```
alias: Backup - Midday
description: Incremental backup run every 12 hours and kept for 2 days
trigger:
  - platform: time_pattern
    hours: /12
condition:
  - condition: time
    after: "00:01:00"
    before: "23:59:00"
action:
  - service: auto_backup.backup_full
    data:
      name: Midday Backup - { { now().strftime('%A %-d %B %Y') } }
      keep_days: 3
  - wait_for_trigger:
      - platform: state
        entity_id:
          - sensor.auto_backup_template
        to: "off"
  - service: hassio.addon_stdin
    data:
      addon: 719b45ef_dropback
      input: sync
```

## Midnight

```
alias: Backup - Midnight
description: >-
  Perform a full HASS backup once a day at 02:30, every day except Monday. They
  are retained for 7 days
trigger:
  - platform: time
    at: "00:00:00"
condition:
  - condition: time
    weekday:
      - tue
      - wed
      - thu
      - fri
      - sat
      - sun
action:
  - service: auto_backup.backup_full
    data:
      name: Midnight Backup - { { now().strftime('%A %-d %B %Y') } }
      keep_days: 6
  - wait_for_trigger:
      - platform: state
        entity_id:
          - sensor.auto_backup_template
        to: "off"
  - service: hassio.addon_stdin
    data:
      addon: 719b45ef_dropback
      input: sync
```

## Weekly

```
alias: Backup - Weekly
description: >-
  Perform a full HASS backup every week, on a Monday at 02:30. It is retained
  for 28 days
trigger:
  - platform: time
    at: "02:30:00"
condition:
  - condition: time
    weekday:
      - mon
action:
  - service: auto_backup.backup_full
    data:
      name: Weekly Backup - { { now().strftime('%A %-d %B %Y') } }
      keep_days: 29
  - wait_for_trigger:
      - platform: state
        entity_id:
          - sensor.auto_backup_template
        to: "off"
  - service: hassio.addon_stdin
    data:
      addon: 719b45ef_dropback
      input: sync
```

# Dashboard

I have two custom buttons on my dashboard. These show the current status of the Home Assistant Backup and the Dropback Sync. When they are active, they flash red, otherwise they are set at 20% Opacity. A quick glance at the dashboard before I do anything effecting the system tells me whether a backup is running or not.

## Lovelace Code for Custom Buttons

```
type: horizontal-stack
cards:
  - type: custom:button-card
    template: basic
    entity: sensor.auto_backup_template
    name: Backup
    show_label: true
    layout: name_state
    styles:
      card:
        - height: 160px
    tap_action:
      action: more-info
      entity: sensor.auto_backup
    state:
      - value: 'on'
        icon: mdi:alert
        label: Active
        styles:
          icon:
            - color: darkred
            - animation: blink 2s ease infinite
          card:
            - border: solid 1px var(--paper-item-icon-active-color)
            - box-shadow: 0px 0px 10px 3px var(--paper-item-icon-active-color)
      - operator: default
        color: white
        icon: mdi:backup-restore
        label: Inactive
        styles:
          card:
            - opacity: 0.2
  - type: custom:button-card
    template: basic
    entity: sensor.dropback_sync
    name: DropBox Sync
    show_label: true
    show_state: false
    styles:
      card:
        - height: 160px
    tap_action:
      action: more-info
      entity: sensor.dropback_sync
    state:
      - value: None
        operator: '!='
        label: |-
          [[[
            return (states['sensor.dropback_sync'].state).substring(15);
          ]]]
        styles:
          icon:
            - color: darkred
            - animation: blink 2s ease infinite
          card:
            - border: solid 1px var(--paper-item-icon-active-color)
            - box-shadow: 0px 0px 10px 3px var(--paper-item-icon-active-color)
      - operator: default
        color: white
        label: Inactive
        styles:
          card:
            - opacity: 0.2
```

# Summary

While my existing backup regime was robust and saved my bacon last week, adopting the additional step of offsite backups has given me additional peace of mind. I am currently checking Dropbox each morning to ensure the previous two backups have been uploaded. Once I get through a couple of weeks and am comfortable the backups are being correctly managed (uploaded/deleted), I'll be able to stop worrying and enjoy my morning coffee without concern!
