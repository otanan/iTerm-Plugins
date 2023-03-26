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


## Installation

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

1. First step
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Import the package
   ```python
   import ytlink
   ```


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.
```python
import numpy as np
import stp
# Dimensionless, time-dependent parameter for self assembly matrix
alpha = lambda t : np.cos(t) + 2
W = stp.self_assembly_rate_matrix(alpha)

# The initial matrix
print(W(0))
# [[-2.  3.  9.]
# [ 1. -3.  0.]
# [ 1.  0. -9.]]

# A later matrix
print(W(1))
# [[-2.          2.54030231  6.45313581]
# [ 1.         -2.54030231  0.        ]
# [ 1.          0.         -6.45313581]]
```


_For more examples, please refer to the [Documentation]._

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

Refer to the [Notion Roadmap] for future features and the state of the project.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact
Created by [Jonathan Delgado](https://jdelgado.net/).


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- [Notion Roadmap]: https://otanan.notion.site/ -->