---
title: GitHub Fail ... and Home Assistant Backups
layout: post
excerpt_separator: "<!--more-->"
date: "2023-03-29 12:33:00 +1100"
categories:
  - github
  - home-assistant
tags:
  - github
  - pages
  - jekyll
  - home-assistant
  - backups
author: mark
header_image: "assets/images/mark-matheson-twitter.png"
---

They say there are four different ways that people learn. These ways are: -

1. Auditory
2. Visual
3. Kinesthetic
4. Reading/Writing

I am definitely the 3rd kind! And boy did I prove that last night with my Git education.

<!--more-->

# Back Story

Having created a branch for the development and deployment of this website, I felt that having all the superfluous Home Assistant files in the `gh-pages` branch was just getting in the way, so I'd clean them up.

I tested this process on a small folder that only had a `.gitkeep` file in it. I was able to delete the folder from the `gh-pages` branch, checkout the `master` branch and it reappeared and then swap back to the `gh-branch` and it was removed again. All good.

# The Fail

So off I went, removing the unneccessary folders and files from the `gh-pages` branch on my local machine, commiting and pushing them to the `gh-pages` branch in GitHub.

It was at this point that I realised that a number of the Home Assistant folders and files were not stored in GitHub 😢

I had just completely deleted things like my Home Assistant database, secrets file and numerous other folders integral to the operation of Home Assistant. To say that my heart sank would be an understatement.

It was also around this time that the thought <q>I really hope my twice daily auto-backups have been working and are acecssible!</q> popped into my head.

# The Recovery

While I check regularly that the backups are appearing in Home Assistant, I had never had a need in a critical situation, to restore one. Sure, I'd tested it in the early days and confirmed the restore process worked, but never under the pressure of needing it to restore the entire system due to a disaster \(well, stupidity really)

Taking a deep breathe, I dove in.

The first thing I did was to make sure that my backups were going to be available after I had reinstalled Home Assistant. That involved copying a few tar files to a secure location.

Reinstalling Home Assistant on Debian isn't that hard. Once that was done, I could start down the track of restoring from a backup.

None of this was quick, and several hours later, as the snapshot was nearing the end of restoring, I was starting to get very nervous.

Thankfully, everything worked perfectly and my monumental stuff up was fixed and my smart home was back again.

# The Moral of the Story

<blockquote>Smart Home, Dumb User!</blockquote>

This highlighted the importance of regular backups. In my case, I have a script in Home Assistant that runs a full backup at midday and midnight, and along with that I retain 6 daily and 4 weekly backups, giving me good coverage in the event of a disaster.

This has proved that my backup stratergy works and that I can recover in the instance of a failure.

In addition, it also highlighted that I need to be more careful before undertaking folder clean ups. Git is great at what it does, but if the files aren't in Git, it can't help me.

# Improvements

It did highlight a weakness. I am currently only keeping my backups on the RPi that hosts Home Assistant. In this instance, that was fine as they were easily accessible. However had I had a catastrophic failure of the RPi, I would've been lost.

Home Assistant is no longer just something I play with in my home lab. It is a mission critical system and I need to treat the data backups with more respect.

I will now be investigating the options to upload them to the cloud. I am aware of a Drop-Box sync package. Time to read up a bit more on that.
