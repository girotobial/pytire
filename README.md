# pytire
[![Documentation Status](https://readthedocs.org/projects/pytire/badge/?version=latest)](https://pytire.readthedocs.io/en/latest/?badge=latest)
![Build Status](https://img.shields.io/github/workflow/status/girotobial/pytire/test)
[![codecov](https://codecov.io/gh/girotobial/pytire/branch/main/graph/badge.svg?token=FRVK7M9PLQ)](https://codecov.io/gh/girotobial/pytire)
[![PyPI Version](https://img.shields.io/pypi/v/pytire)](https://pypi.org/project/pytire/)
[![Licence](https://img.shields.io/github/license/girotobial/pytire)](https://github.com/girotobial/pytire/blob/main/LICENSE)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A library to make interpreting tire attributes and calculations easier.

### Table of Contents
  * [Table of Contents](#table-of-contents)
  * [Getting Started](#getting-started)
  * [Dev Setup](#dev-setup)
## Getting Started
To use this library install it via pip

```sh
$ pip install pytire
```

Usage
```python
>>> from pytire import Tire
>>> tire = Tire("34x10.75-16")
>>> tire.diameter
0.8636...

>>> tire.width
0.27305...

>>> tire.inner_diameter
0.4064...

>>> tire.volume()
0.203642044328
```
[The Docs are here.](https://pytire.readthedocs.io/en/latest/)
## Dev Setup

Clone from github
```
$ git clone 
```

Install using poetry
```sh
$ poetry install
```
set up pre-commit
```sh
$ pre-commit install
```

Alternatively use the dev container.
