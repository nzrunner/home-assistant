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

# Matho's Git Guide

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

- [Usage Guide](#usage-guide)
- [Project Git Guide](#project-git-guide)
- [Change Log](#change-log)
- [Resources](#resources)
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

<!-- GIT GUIDE -->

---

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

<ul>
<li>https://herewecode.io/blog/a-beginners-guide-to-git-how-to-write-a-good-commit-message/</li>
<li>https://herewecode.io/blog/a-beginners-guide-to-git-what-is-a-changelog-and-how-to-generate-it/</li>
<li>https://keepachangelog.com/en/1.1.0/</li>
<li>https://www.conventionalcommits.org/en/v1.0.0/</li>
<li>https://udacity.github.io/git-styleguide/</li>
</ul>

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
