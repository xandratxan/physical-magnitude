# Package physical-magnitude

> Simple operations with magnitudes including units and uncertainties.
 
| Last version: 0.1.0          | Source code: [GitHub](https://github.com/xandratxan/physical-magnitude/)             | Issues: [GitHub](https://github.com/xandratxan/physical-magnitude/issues/) |
|------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------|
| **Last release: March 2023** | **Documentation : [GitHub Pages](https://xandratxan.github.io/physical-magnitude/)** | **License: GNU GPL 3.0**                                           |

The package ``physical-magnitude`` allows to perform simple operations with magnitudes including units and uncertainties.
It allows to define magnitudes with value, uncertainty and unit.
It allows to compute simple operations providing the result not only for the magnitude value,
but also its uncertainty and unit.
Available operations include summation, subtraction, multiplication and division.

## Installation

``physical-magnitude`` can be installed in three different ways.

Install via pip after downloading the package from GitHub:

Install via pip from PyPi-like server:

```bash
pip install physical-magnitude --extra-index-url https://xandratxan.github.io/python-package-server/
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
m1 = Magnitude(value=10, uncertainty=1, unit='m')
m2 = Magnitude(value=20, uncertainty=2, unit='m')
print(f'm1: {m1}')
print(f'm2: {m2}\n')

# Sum magnitudes
m_sum = m1 + m2
print(f'Sum: {m_sum}\n')

# Subtract magnitudes
m_dif = m2 - m1
print(f'Subtract: {m_dif}\n')

# Multiply magnitudes
m_prod = m1 * m2
print(f'Multiply: {m_prod}')
m_prod.unit = 'm²'
print(f'Multiply: {m_prod}\n')

# Divide magnitudes
m_div = m2 / m1
print(f'Divide: {m_div}')
m_div.unit = ''
print(f'Divide: {m_div}\n')
```

Output:

```
m1: 10 ± 1 m (10.0%)
m2: 20 ± 2 m (10.0%)

Sum: 30 ± 2.23606797749979 m (7.4535599249993%)

Subtract: 10 ± 2.23606797749979 m (22.360679774997898%)

Multiply: 200 ± 28.284271247461906 (m)·(m) (14.142135623730953%)
Multiply: 200 ± 28.284271247461906 m² (14.142135623730953%)

Divide: 2.0 ± 0.28284271247461906 (m)/(m) (14.142135623730953%)
Divide: 2.0 ± 0.28284271247461906  (14.142135623730953%)
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

Contributors:
: Ricardo Gomez, 
[@GitHub](https://github.com/ricargoes/)