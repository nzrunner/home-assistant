---
layout: page
title: "Git Guide"
permalink: /git-guide/
---

![Logo]({{ site.baseurl }}/assets/images/mark-matheson-digital-business-consultant.png)

## Usage Guide

To get the most benefit out of the ChangeLog module, the commit messages have to be in this format:

```
type(category): description [flags]
```

Where `type` is one of the following:

- `breaking`
- `build`
- `ci`
- `chore`
- `docs`
- `feat`
- `fix`
- `other`
- `perf`
- `refactor`
- `revert`
- `style`
- `test`

Where `flags` is an optional comma-separated list of one or more of the following (must be surrounded in square brackets):

- `breaking`: alters `type` to be a breaking change

And `category` can be anything of your choice. If you use a type not found in the list (but it still follows the same format of the message), it'll be grouped under `other`.

## Project Git Guide

The types I am standardising on for this project are as follows: -

- `docs`
  - All changes to the README, GIT-GUIDE and CHANGELOG documents
- `fix`
  - Any issue tagged as 'bug' along with any code changes that fix a bug
- `feat`
  - Any issue tagged as 'feature request' along with any code changes that add a new feature
- `chore`
  - Any changes like system updates, adding images or untracked files
- `other`
  - Any other changes not covered by the above

## Change Log

From within the Home Assistant folder, run the following: -

```bash
changelog generate
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- RESOURCES -->

## Resources

This is currently just a dumping ground for git recources that I have found.

- <https://herewecode.io/blog/a-beginners-guide-to-git-how-to-write-a-good-commit-message>
- <https://herewecode.io/blog/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/>
- <https://keepachangelog.com/en/1.1.0/>
- <https://www.conventionalcommits.org/en/v1.0.0/>
- <https://udacity.github.io/git-styleguide/>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
