# Package physical-magnitude

> Simple operations with magnitudes including units and uncertainties.

| Last version: 0.1.0| Source code: [GitHub](https://github.com/xandratxan/physical-magnitude) | Issues: [GitHub](https://github.com/xandratxan/physical-magnitude/issues) |
|------------------------------|------------------------------|------------------------------|
| **Last release: March 2023** | **Documentation : [GitHub Pages](https://xandratxan.github.io/metpy/docs/physical-magnitude/index.html)** | **License: GNU GPL 3.0**|

> **WARNING**: This package is under active development. The current version is considered non-stable..

This package allows to perform simple operations with magnitudes including units and uncertainties. It allows to define magnitudes with value, uncertainty and unit. It allows to compute simple operations providing the result not only for the magnitude value, but also its uncertainty and unit.Available operations include summation, subtraction, multiplication and division.

## Installation

``physical-magnitude`` can be installed in three different ways.

Install via pip from PyPi-like server:

```bash
pip install physical-magnitude --extra-index-url https://xandratxan.github.io/metpy/server/
```

Install via pip with GitHub repository url:

```bash
pip install git+https://github.com/xandratxan/physical-magnitude.git#egg=physical-magnitude
```

Clone GitHub repository and install via pip:

```bash
 git clone git@github.com:xandratxan/physical-magnitude.git
 cd physical-magnitude
 pip install .
```

## Usage

```python
from magnitude import Magnitude

# Define magnitudes
m1 = m1 = Magnitude(value=100, unit='m', uncertainty=1)
m2 = m2 = Magnitude(value=200, unit='m', uncertainty=2)
print(f'm1: {m1}')
print(f'm2: {m2}')

# Sum magnitudes
m_sum = m1 + m2
print(f'Sum: {m_sum}')

# Subtract magnitudes
m_dif = m2 - m1
print(f'Subtract: {m_dif}')

# Multiply magnitudes
m_prod = m1 * m2
print(f'Multiply: {m_prod}')
m_prod.unit = 'm²'
print(f'Multiply: {m_prod}')

# Divide magnitudes
m_div = m2 / m1
print(f'Divide: {m_div}')
m_div.unit = ''
print(f'Divide: {m_div}')
```


Output:

```
m1: 100.0 ± 1.0 m (1.0%)
m2: 200.0 ± 2.0 m (1.0%)

Sum: 300.0 ± 2.23606797749979 m (0.74535599249993%)

Subtract: 100.0 ± 2.23606797749979 m (2.23606797749979%))

Multiply: 20000.0 ± 282.842712474619 (m)·(m) (1.4142135623730951%)
Multiply: 20000.0 ± 282.842712474619 m² (1.4142135623730951%)

Divide: 2.0 ± 0.0282842712474619 (m)/(m) (1.4142135623730951%)
Divide: 2.0 ± 0.0282842712474619  (1.4142135623730951%)
```


## Release History

* 0.1.0
    * First release


## Authors and contributors

Author:
: Xandra Campo,
[@GitHub](https://github.com/xandratxan/)
[@GitHub Pages](https://xandratxan.github.io/),
xkmpera@gmail.com

