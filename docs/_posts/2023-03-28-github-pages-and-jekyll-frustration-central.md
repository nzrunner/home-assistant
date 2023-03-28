---
layout: post
excerpt_separator: <!--more-->
title: "GitHub Pages and Jekyll - Frustration Central!"
date: 2023-03-28 18:33:00 +1100
categories: github
tags: [github, pages, jekyll]
---

![Logo]({{ site.baseurl }}/assets/images/mark-matheson-digital-business-consultant.png)

As part of my GitHub learning, I have tried to use as many of the available features as possible. I identified two features that I wasn't using: -

1. GitHub Pages (AKA Websites)
2. Wiki

<!--more-->

So I figured, "what the heck, it can't be that hard, let's deploy a website". Conceptually, a really simple idea, but in practice an experience fraught with angst and anger.

Now let's be honest, I may have bought some of the angst on myself by trying to implement several modifcations to the basic model before actually deploying the basic model and testing it. And, to be fair, now I have it all running (this blog is the outcome), it's a really simple platform to maintain and update.

So, what's involved?

In a couple of overly simplified steps: -

1. Create a repo or use a branch in an existing repo
2. Create a website in that repo/branch
3. Tell GitHub to deploy the website to GitHub Pages

I wanted my website to inherit the folder name of my repo, so needed to use the branch option, rather than creating a new report.

My first mistake was choosing to publish a website using [custom GitHub Actions workflow 🔗](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow). Despite it being possible, and after numerous commits to force a build and deploy, I never got any positive outcomes. No website visible and frustration raging through my veins.

![Frustration]({{ site.baseurl }}/assets/images/frustration.png)

So I decided to try a different tact, and use the option to [publish from a branch 🔗](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow) of my existing repo.

It was at this stage that I realised that although I could publish a very basic, static website using this method, it didn't give me what Jekyll offered. Having heard all about [Jekyll 🔗](https://jekyllrb.com/) and how it was designed to work with [GitHub Pages 🔗](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll), I was keen to use it.

So down the next rabbit hole I went!

It was at this point that I came to the realisation that in order to use Jekyll, I was going to need to install a few things on my local machine in order to deploy it. I had hoped that it would be a web-based solution, but I realised that it required local configuration and then used Git to push it to GitHub. It was at this stage that it could be built and deployed to GitHub Pages.

So the first thing I did was follow the [prerequisites 🔗](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site) outlined in the documentation. This got me up and running with Ruby and the necessary gems.

Thankfully, GitHub's documentation appeared to provide a good guide to [creating a site 🔗](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll#creating-your-site), so I started to follow it. I already had my repo and had a folder ready to use, so off I went.

It was at this point, I shot myself in the foot!

![Shooting in the foot]({{ site.baseurl }}/assets/images/shooting-in-foot.jpg)

As part of the process, I decided I didn't like the default theme, so I would use a custom theme. Again, GitGub provides really good [documentation 🔗](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll) for doing this. In retrospect, it would've been much smarter to use the default theme, get a website successfully published, and then change the theme. Meaning, if I broke something, I could use Git to revert back a few steps. Hindsight is a wonderful thing ☹

Now I had a website that was completely empty, nothing on the front page, and when I tried to access any sub-page, I got the expected header and footer with a 404 error. It was at this stage I decided that going to bed was a better option than reverting to alcohol. After all, I had already pulled out clumps of hair, something I can ill afford to lose.

I woke up the next day (this morning as it happens), determined to figure out what I had done wrong.

With the calrity of a new day, it didn't take me long to realise that the sample markdown files provided by the default theme didn't work with the custom theme. A by-product of cvhanging themes mid-install. Renaming a few files produced a basic website that used the custom theme, and looked like what I was expecting from Jekyll. Success!

Now I could start reading into the plugins and finer points of customising the theme and start to build a website that looked like something I wanted to produce. Ironically, I abandoned the custom theme I had originally planned on using and settled on the Hamilton, the one I am using now. If you want a few places to check out custom Jekyll themes, have a look [here 🔗](https://jekyllrb.com/docs/themes/).

So after hours of frustration and angst, I have a working website. Adding a new blog post is as easy as creating a markdown file in the \_posts folder with an [appropriate name 🔗](https://jekyllrb.com/docs/posts/) and pushing the change to GitHub.

If you;ve got to the end of this post, hopegully you can avoid much of the angst and frustration I encountered and be able to quickly publish a Jekyll website for your GitHub repsitory. Let me know if the comments below.
