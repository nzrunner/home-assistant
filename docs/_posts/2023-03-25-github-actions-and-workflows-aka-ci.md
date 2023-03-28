---
layout: post
title: "GitHub Actions and Workflows (AKA CI)"
excerpt_separator: <!--more-->
date: 2023-03-25 22:00:00 +1100
categories: home-assistant github
tags: [github, home-assistant, actions, workflows, ci]
author: Mark Matheson
---

Exploring other people's Git repositories led me to investing time in learning about GitHub actions. All I can say is wow! My programming skills are OK at best, but learning from others in the open-source community has resulted in me now having some awesome CI workflows running on my Git repository, making life so much easier.

![GitHub CI]({{ site.baseurl }}/assets/images/github-ci.png)

<!--more-->

In addition, I learnt about Git pre-commit hooks, and have a few of these running on my RPi, meaning the code I upload is much cleaner.

I have adopted a similar approach to [@frenck](https://github.com/frenck) and [@metbril](https://github.com/metbrill) and have enhanced how my configuration file is split up. It was difficult to understand at first, but once I understood the structure, it made perfect sense. For anyone even mildly interested, it is definitely worth investing the time and effort. Links to their configurations provided below: -

- @Frenck - <https://github.com/frenck/home-assistant-config>
- @Metbril - <https://github.com/metbril/home-assistant-config>

As a result of these major changes in my Git repository, my Home Assistant configuration is cleaner and much easier to understand.

A huge 🙏 thank you to the open-source community!
