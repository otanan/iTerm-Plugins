<!-- Filename:      README.md -->
<!-- Author:        Jonathan Delgado -->
<!-- Description:   GitHub README -->

<!-- Header -->
<h2 align="center">iTerm Plugins</h2>
  <p align="center">
    Various small plugins written for iTerm2 using <a href="https://github.com/otanan/iTermLink">iTermLink</a> library.
    <br />
    <br />
    Status: <em>in progress</em>
    <!-- Documentation link -->
    <!-- ·<a href="https://stochastic-thermodynamics-in-python.readthedocs.io/en/latest/"><strong>
        Documentation
    </strong></a> -->
    <!-- Notion Roadmap link -->
    ·<a href="https://otanan.notion.site/iTheme-f8b8eff9c31449c9a56d6a6c17ddf63e"><strong>
        Notion Roadmap for iTheme »
    </strong></a>
  </p>
</div>


<!-- Project Demo -->
<!-- https://user-images.githubusercontent.com/6320907/189829171-1e91c3e2-0feb-4e7a-aa12-0a4d899f059b.mp4 -->


<!-- ## Table of contents
* [Contact](#contact)
* [Acknowledgments](#acknowledgments) -->


### iTheme

https://user-images.githubusercontent.com/6320907/227763351-661866f1-95ae-44bd-b2a9-62f9ac00fc45.mov

<!-- ### iTerm Build -->


<!-- ### Wallp(aper) -->

## Installation

1. Install the [iTermLink repo][iTermLink].
2. Clone this repo.
3. Follow the installation instructions for the plugin of choice.

### iTheme
1. Go to [iTerm2 Color Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes) repository and follow their instructions to download all available or desired color schemes.
2. Import them into iTerm.
3. Alias the command to run this script
```bash
alias itheme=python3 path/to/itheme.py
```
4. (Optional) Add the following line to your Send Text at Start command to have it generate each time a new window is opened.
```bash
clear && itheme --auto
```
The ```bash --auto``` flag is to instruct the program that this command was run automatically and should not always be listened to. In this case it avoids changing the theme each time a new _tab_ is opened. Instead it only changes with new _windows_.


<!-- ### iTerm Build -->


<!-- ### Wallp(aper) -->



<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
```bash
```


_For more examples, please refer to the [Documentation]._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

Refer to the [Notion Roadmap] for future features and the state of the project.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
Created by [Jonathan Delgado](https://jdelgado.net/).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

[iTermLink]: https://github.com/otanan/iTermLink