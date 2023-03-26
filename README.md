<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<a href="https://github.com/TahsinCr/python-linqex/blob/master/README.md">
 <img src="images/languages/british-flag.png" height="28" alt="Logo" ></a>
<a href="https://github.com/TahsinCr/python-linqex/blob/master/README_tr.md">
 <img src="images/languages/turkish-flag.png" height="28" alt="Logo" ></a>

<br />






<!-- About -->
<div align="center">

<a href="https://github.com/TahsinCr/python-linqex">

<img src="images/logo.png" alt="Logo">

</a>

<h3 align="center">Python Linqex</h3>

<p align="center">

The linq module in C# has been adapted for python with some modifications.

<a href="https://github.com/TahsinCr/python-linqex/blob/master/CHANGELOG.md">Changelog</a>
 · 
<a href="https://github.com/TahsinCr/python-linqex/issues">Report Bug</a>
 · 
<a href="https://github.com/TahsinCr/python-linqex/issues">Request Feature</a>
 
</p>

</div>






<!-- TABLE OF CONTENTS -->

<details>

<summary>Table of Contents</summary>

<ol>

<li>

<a href="#about-the-project">About The Project</a>

<ul>

<li><a href="#built-with">Built With</a></li>

</ul>

</li>

<li>

<a href="#getting-started">Getting Started</a>

<ul>

<li><a href="#prerequisites">Prerequisites</a></li>

<li><a href="#installation">Installation</a></li>

</ul>

</li>

<li><a href="#usage">Usage</a></li>

<li><a href="#roadmap">Roadmap</a></li>

<li><a href="#contributing">Contributing</a></li>

<li><a href="#license">License</a></li>

<li><a href="#contact">Contact</a></li>

<li><a href="#acknowledgments">Acknowledgments</a></li>

</ol>

</details>






<!-- ABOUT THE PROJECT -->

##  About The Project

Provides simple to use LINQ features to Python 3.x.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

###  Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- GETTING STARTED -->

##  Getting Started

To get a local copy up and running follow these simple example steps.

###  Prerequisites

Does not require any prerequisites

###  Installation

1. Clone the repo
```sh
git clone https://github.com/TahsinCr/python-linqex.git
```

2. Install PIP packages
```sh
pip install linqex
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- USAGE EXAMPLES -->

##  Usage

Let's have different customers. Let's choose the male ones among these customers. For this:
```python
from linqex.linq import Enumerable
customers_list = [
    {'name' : 'Jonh', 'age' : 25, 'gender': 'male'}
    {'name' : 'Emma', 'age' : 44, 'gender': 'female'}
    {'name' : 'Steve', 'age' : 17, 'gender': 'male'}
]

customers_enumerable = Enumerable(customers_list)

# to select only male ones:
customers_male_enumerable = customers_enumerable.Where(lambda key,value: value['gender'] == 'male')

for customer in customers_male_enumerable.ToValue:
    print(customer)
```
Output
```
{'name' : 'Jonh', 'age' : 25, 'gender': 'male'}
{'name' : 'Steve', 'age' : 17, 'gender': 'male'}
```

_For more examples, please refer to the [Documentation](https://github.com/TahsinCr/python-linqex/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- ROADMAP -->

##  Roadmap

- [x] Add Changelog

- [x] Add Test File

- [x] Bugs Fixed

- [ ] Add Documents

- [ ] Add Additional Templates w/ Examples

See the [open issues](https://github.com/TahsinCr/python-linqex/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTRIBUTING -->

##  Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project

2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)

3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)

4. Push to the Branch (`git push origin feature/AmazingFeature`)

5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- LICENSE -->

##  License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- CONTACT -->

##  Contact

Tahsin Çirkin - [@TahsinCrs](https://twitter.com/TahsinCrs) - TahsinCr@outlook.com

Project Link: [https://github.com/TahsinCr/python-linqex](https://github.com/TahsinCr/python-linqex)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- ACKNOWLEDGMENTS -->

##  Acknowledgments

* [PyPI](https://pypi.org/project/linqex)

* [C-Sharp Linq Documents](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- LINKS & IMAGES URL -->

[contributors-shield]: https://img.shields.io/github/contributors/TahsinCr/python-linqex.svg?style=for-the-badge

[contributors-url]: https://github.com/TahsinCr/python-linqex/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/TahsinCr/python-linqex.svg?style=for-the-badge

[forks-url]: https://github.com/TahsinCr/python-linqex/network/members

[stars-shield]: https://img.shields.io/github/stars/TahsinCr/python-linqex.svg?style=for-the-badge

[stars-url]: https://github.com/TahsinCr/python-linqex/stargazers

[issues-shield]: https://img.shields.io/github/issues/TahsinCr/python-linqex.svg?style=for-the-badge

[issues-url]: https://github.com/TahsinCr/python-linqex/issues

[license-shield]: https://img.shields.io/github/license/TahsinCr/python-linqex.svg?style=for-the-badge

[license-url]: https://img.shields.io/github/forks/TahsinCr/python-linqex?style=flat-square

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/TahsinCr

[Python]: https://img.shields.io/pypi/pyversions/linqex?style=flat-square

[Python-url]: https://pypi.org/project/linqex