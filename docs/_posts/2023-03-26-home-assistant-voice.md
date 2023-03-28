---
layout: post
excerpt_separator: <!--more-->
title: "Home Assistant Voice"
date: 2023-03-26 22:16:00 +1100
categories: home-assistant
tags: [home-assistant, voice, conversation]
author: Mark Matheson
---

I spent some time trying to get Home Assistant Voice working. I found it to be an extremely frustrating experience. The documentation while comprehensive, is confusing and disjointed. Just my humble opinion.

<!--more-->

I am pleased to say, I have it working within the app, albeit only in a browser on my laptop and not in the app on my mobile devices.[^1] I suspect this is related to my http intergration, despite the fact both my internal and external URL's are using https. I'm not going to spend too much time diagnosing that at the moment, as with Siri integration working, it is actually useful already.

For my conversation integration, the two files I needed to create were `includes/intent_script.yaml` and `custom_sentences/en/domestic.yaml`. The later file can be named anything, but must be in the custom_sentences/{language} folder. You can have multiple of these files, broken down into logical groups.

The code I currently have in each of them is as follows: -

### includes/intent_script.yaml

```
#################################################################################
#
#  _       _             _                     _       _
# (_)_ __ | |_ ___ _ __ | |_     ___  ___ _ __(_)_ __ | |_
# | | '_ \| __/ _ \ '_ \| __|   / __|/ __| '__| | '_ \| __|
# | | | | | ||  __/ | | | |_    \__ \ (__| |  | | |_) | |_
# |_|_| |_|\__\___|_| |_|\__|___|___/\___|_|  |_| .__/ \__|
#                          |_____|              |_|
#
#################################################################################

# For the Assist/Conversation intergration
intent_script:
  YearOfVoice:
    speech:
      text: "Great! We're at over 40 languages and counting."

  HangTheLaundry:
    speech:
      text: "The laundry has been hung"
    action:
      service: automation.trigger
      target:
        entity_id: automation.laundry_status

  LaundryInside:
    speech:
      text: "The laundry has been brought inside"
    action:
      service: automation.trigger
      target:
        entity_id: automation.laundry_status

  BinsOut:
    action:
      service: automation.trigger
      target:
        entity_id: automation.system_rubbish_status
    speech:
      text: "The rubbish bins are out"

  BinsIn:
    action:
      service: automation.trigger
      target:
        entity_id: automation.system_rubbish_status
    speech:
      text: "The rubbish bins are in"

  GoodMorning:
    action:
      service: automation.trigger
      target:
        entity_id: automation.good_morning
    speech:
      text: "Good Morning!"

  GoodNight:
    action:
      service: automation.trigger
      target:
        entity_id: automation.good_night
    speech:
      text: "Good Night!"
```

### custom_sentences/en/domestic.yaml

```
#################################################################################
#
#        _                           _   _
#     __| | ___  _ __ ___   ___  ___| |_(_) ___
#    / _` |/ _ \| '_ ` _ \ / _ \/ __| __| |/ __|
#   | (_| | (_) | | | | | |  __/\__ \ |_| | (__
#    \__,_|\___/|_| |_| |_|\___||___/\__|_|\___|
#
#
#################################################################################

language: "en"
intents:
  YearOfVoice:
    data:
      - sentences:
          - "how is the year of voice going"

  HangTheLaundry:
    data:
      - sentences:
          - "[hang][ing] [the] laundry [out]"

  LaundryInside:
    data:
      - sentences:
          - "[bring][ing] [the] laundry in"

  BinsOut:
    data:
      - sentences:
          - "[put] [the] bins out"

  BinsIn:
    data:
      - sentences:
          - "[bring] [the] bins in"

  GoodMorning:
    data:
      - sentences:
          - "good morning"

  GoodNight:
    data:
      - sentences:
          - "good night"
```

Although I have several Google Home devices, I am not comfortable with the Google servers being "fed" all the data relating to my devices, so won't be adding the Google Home integration at this point. Besides, it's a lot of work for little benefit. Check out the integration - <https://www.home-assistant.io/integrations/google_assistant/>

I guess it's back to talking to myself again when I want my smart home to do something. \<ponders>

#### Notes

[^1]: I finally stumbled on the Apple iPhone Shortcuts that I needed to make it work on my mobile devices (<https://www.home-assistant.io/docs/assist/apple>), and "Hey Siri, Assist" is now working nicely but still no joy getting voice working from within the mobile app.
