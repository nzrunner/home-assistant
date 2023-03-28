---
layout: post
title: "Home Assistant Voice"
excerpt_separator: <!--more-->
date: 2023-03-26 22:16:00 +1100
categories: home-assistant
tags: [home-assistant, voice, conversation]
---

![Logo]({{ site.baseurl }}/assets/images/mark-matheson-digital-business-consultant.png)

I spent some time trying to get Home Assistant Voice working. I found it to be an extremely frustrating experience. The documentation while comprehensive, is confusing and disjointed. Just my humble opinion.

<!--more-->

I am pleased to say, I have it working within the app, albeit only in a browser on my laptop and not in the app on my mobile devices. I suspect this is related to my http intergration, despite the fact both my internal and external URL's are using https.

_Note: Finally stumbled on the Apple iPhone Shortcuts that I needed to make it work on my mobile devices, and "Hey Siri, Assist" is working nicely but still no joy getting voice working from within the mobile app._

For my conversation integration, the two files I needed to create were [includes/intent_script.yaml][/includes/intent_script.yaml] and [custom_sentences/en/domestic.yaml][custom_sentences/en/domestic.yaml]. The later file can be named anything, but must be in the custom_sentences/{language} folder.

Although I have several Google Home devices, I am not comfortable with the Google servers being "fed" all the data relating to my devices, so won't be adding the Google Home integration at this point. Besides, it's a lot of work for little benefit.

So, guess it's back to talking to myself again when I want my smart home to do something. \<ponders>
