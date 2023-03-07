# Package magnitudes

> Simple operations with magnitudes including units and uncertainties.

This package allows to perform simple operations with magnitudes including units and uncertainties.
It allows to define magnitudes with value, uncertainty and unit.
It allows to compute simple operations providing the result not only for the magnitude value,
but also its uncertainty and unit.
Available operations include summation, subtraction, multiplication and division.

## Installation

Installation for local usage:

```bash
git clone git@github.com:xandratxan/magnitudes.git
cd magnitudes
pip install .
```

## Usage examples

### Defining a magnitude

#### How magnitudes can be defined

Magnitudes are defined as instantiations of the class ``Magnitude``.

```python
from magnitude.magnitude import Magnitude
```

Magnitudes must have value, uncertainty and unit.
If absolute uncertainty is provided, relative uncertainty will be calculated:

```python
Magnitude(value=20, unit='m', uncertainty=2)
20 ± 2 m (10.0%)
```

If relative uncertainty is provided, absolute uncertainty will be calculated:

```python
Magnitude(value=30, unit='m', relative_uncertainty=0.1)
30 ± 3.0 m (10.0%)
```

If both uncertainties are provided, the agreement between values will be checked.
If both uncertainties are equivalent, the magnitude will be defined correctly:

```python
Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
20 ± 2 m (10.0%)
```

If both uncertainties are not equivalent, an exception will be raised:

```python
Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
    self.complete_uncertainties()
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 60, in complete_uncertainties
    raise ValueError('Absolute and relative uncertainties do not match.')
ValueError: Absolute and relative uncertainties do not match.
```

Magnitudes without uncertainties may be defined with zero uncertainty.

```python
Magnitude(value=20, unit='m', uncertainty=0)
20 ± 0 m (0.0%)
```

```python
Magnitude(value=20, unit='m', relative_uncertainty=0)
20 ± 0 m (0%)
```

```python
Magnitude(value=20, unit='m', uncertainty=0, relative_uncertainty=0)
20 ± 0 m (0%)
```

#### How magnitudes cannot be defined

Magnitudes must have uncertainties. They cannot be defined with no uncertainties:

```python
Magnitude(value=10, unit='m')
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
    self.complete_uncertainties()
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 70, in complete_uncertainties
    raise TypeError('Magnitudes must have uncertainties.')
TypeError: Magnitudes must have uncertainties.
```

Magnitudes cannot be defined with negative uncertainties, since it have no physical meaning:

```python
Magnitude(value=20, unit='m', uncertainty=-2)
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
    self.complete_uncertainties()
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 72, in complete_uncertainties
    raise ValueError('Uncertainties must be positive.')
ValueError: Uncertainties must be positive.
```

```python
Magnitude(value=30, unit='m', relative_uncertainty=-0.1)
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
    self.complete_uncertainties()
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 72, in complete_uncertainties
    raise ValueError('Uncertainties must be positive.')
ValueError: Uncertainties must be positive.
```

### Simple operations with magnitudes

First, define some magnitudes to operate with them:

```python
m1 = Magnitude(value=10, unit='m', uncertainty=1)
m2 = Magnitude(value=20, unit='m', uncertainty=2)
m3 = Magnitude(value=20, unit='cm', uncertainty=2)
m4 = Magnitude(value=20, unit='m²', uncertainty=2)
```

Magnitudes can be summed or subtracted as long as they have the same units:

```python
m1 + m2
30 ± 2.23606797749979 m (7.4535599249993%)
```

```python
m2 - m1
10 ± 2.23606797749979 m (22.360679774997898%)
```

If they have different units, an exception will be raised:

```python
m2 + m3
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 22, in __add__
    raise TypeError('Added magnitudes must have the same units.')
TypeError: Added magnitudes must have the same units.
```

```python
m2 - m3
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 31, in __sub__
    raise TypeError('Subtracted magnitudes must have the same units.')
TypeError: Subtracted magnitudes must have the same units.
```

Magnitudes can be multiplied or divided independently of their units.
The unit resulting from the product or the division will be the concatenation of the individual magnitudes:

```python
m1 * m2
200 ± 28.284271247461906 m·m (14.142135623730953%)
```

```python
m2 / m1
2.0 ± 0.28284271247461906 m/m (14.142135623730953%)
```

Multiple magnitudes can be summed and/or subtracted as long as they have the same units:

```
m1 + m2 + m1 - m2
20 ± 3.1622776601683795 m (15.811388300841896%)
```

Multiple magnitudes can be multiplied and/or divided independently of their units:

```
m1 * m2 / m3
10.0 ± 1.7320508075688776 m·m/cm (17.320508075688775%)
```

However, combining summation/subtraction with product/division require some user work.
Trying to do m1 * m2 + m4 will raise an error since the units of m1 * m2 are m·m while the units of m4 are m².

```
m1 * m2 + m4
Traceback (most recent call last):
  File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
  File "<input>", line 1, in <module>
  File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 68, in __add__
    raise TypeError('Added magnitudes must have the same units.')
TypeError: Added magnitudes must have the same units.
```

First, we need to define a new magnitude m as m1 * m2, then change the unit of m from m·m to m², and finally we can do m + m4 

```
m = m1 * m2
m
200 ± 28.284271247461906 m·m (14.142135623730953%)
m.unit = 'm²'
m
200 ± 28.284271247461906 m² (14.142135623730953%)
m + m4
220 ± 28.354893757515654 m² (12.888588071598026%)
```

## Release History

* 0.1.0
    * First release

## Source code, license and author

Source code of the package available on [GitHub.](https://github.com/xandratxan/magnitudes)
Distributed under the GNU General Public license. See ``LICENSE`` for more information.

Xandra Campo [@GitHub](https://github.com/xandratxan) – xkmpera@gmail.com
