User Guide
==========

This page gives a good introduction in how to get started with ``magnitudes``.

Installation
------------

``magnitudes`` can be installed via pip after downloading the package from GitHub:

.. code-block::

    git clone git@github.com:xandratxan/magnitudes.git
    cd magnitudes
    pip install .

How to define a magnitude
-------------------------

Magnitudes are defined as instantiations of the class ``Magnitude``:

.. code-block::

   from magnitude import Magnitude

Magnitudes must have value, uncertainty and unit.
If absolute uncertainty is provided, relative uncertainty will be calculated:

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=2)
    20 ± 2 m (10.0%)

If relative uncertainty is provided, absolute uncertainty will be calculated:

.. code-block::

    Magnitude(value=30, unit='m', relative_uncertainty=0.1)
    30 ± 3.0 m (10.0%)

If both uncertainties are provided, the agreement between values will be checked.
If both uncertainties are equivalent, the magnitude will be defined correctly:

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
    20 ± 2 m (10.0%)

If both uncertainties are not equivalent, an exception will be raised:

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 70, in __init__
        self._magnitude_consistency_check()
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 134, in _magnitude_consistency_check
        raise ValueError('Absolute and relative uncertainties do not match.')
    ValueError: Absolute and relative uncertainties do not match.

Magnitudes without uncertainties may be defined with zero uncertainty:

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=0)
    20 ± 0 m (0.0%)

.. code-block::

    Magnitude(value=20, unit='m', relative_uncertainty=0)
    20 ± 0 m (0%)

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=0, relative_uncertainty=0)
    20 ± 0 m (0%)

Magnitudes can defined with zero value, but they may be tricky: uncertainties may not have physical meaning:

.. code-block::

    Magnitude(value=0, unit='m', uncertainty=0.1)
    0 ± 0.1 m (inf%)

.. code-block::

    Magnitude(value=0, unit='m', relative_uncertainty=0.1)
    0 ± 0.0 m (10.0%)

How not to define magnitude
---------------------------

Magnitudes must have uncertainties. They cannot be defined with no uncertainties:

.. code-block::

    Magnitude(value=10, unit='m')
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 70, in __init__
        self._magnitude_consistency_check()
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 147, in _magnitude_consistency_check
        raise TypeError('Magnitudes must have uncertainties.')
    TypeError: Magnitudes must have uncertainties.

Magnitudes cannot be defined with negative uncertainties, since it has no physical meaning:

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=-2)
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 70, in __init__
        self._magnitude_consistency_check()
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 149, in _magnitude_consistency_check
        raise ValueError('Uncertainties must be positive.')
    ValueError: Uncertainties must be positive.

.. code-block::

    Magnitude(value=30, unit='m', relative_uncertainty=-0.1)
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 70, in __init__
        self._magnitude_consistency_check()
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 149, in _magnitude_consistency_check
        raise ValueError('Uncertainties must be positive.')
    ValueError: Uncertainties must be positive.

Sum and subtract magnitudes
---------------------------

First, define some magnitudes to operate with them:

.. code-block::

    m1 = Magnitude(value=10, unit='m', uncertainty=1)
    m2 = Magnitude(value=20, unit='m', uncertainty=2)
    m3 = Magnitude(value=20, unit='cm', uncertainty=2)

Magnitudes can be summed or subtracted as long as they have the same units:

.. code-block::

    m1 + m2
    30 ± 2.23606797749979 m (7.4535599249993%)

.. code-block::

    m2 - m1
    10 ± 2.23606797749979 m (22.360679774997898%)

If they have different units, an exception will be raised:

.. code-block::

    m1 + m3
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 83, in __add__
        raise TypeError('Added magnitudes must have the same units.')
    TypeError: Added magnitudes must have the same units.

.. code-block::

    m2 - m3
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 93, in __sub__
        raise TypeError('Subtracted magnitudes must have the same units.')
    TypeError: Subtracted magnitudes must have the same units.

Multiply and divide magnitudes
------------------------------

Magnitudes can be multiplied or divided independently of their units.
The unit resulting from the product or the division will be the concatenation of the individual magnitudes:

.. code-block::

    m1 * m2
    200 ± 28.284271247461906 m·m (14.142135623730953%)

.. code-block::

    m2 / m1
    2.0 ± 0.28284271247461906 m/m (14.142135623730953%)

Combining summation/subtraction with product/division
-----------------------------------------------------

Multiple magnitudes can be summed and/or subtracted as long as they have the same units:

.. code-block::

    m1 + m2 + m1 - m2
    20 ± 3.1622776601683795 m (15.811388300841896%)


Multiple magnitudes can be multiplied and/or divided independently of their units:

.. code-block::

    m1 * m2 / m3
    10.0 ± 1.7320508075688776 m·m/cm (17.320508075688775%)

However, combining summation/subtraction with product/division require some units management.
Trying to do ``m1 * m2 + m4`` will raise an error since the units of ``m1 * m2`` are ``'m·m'`` while the units of ``m4`` are ``'m²'``.

.. code-block::

    m1 * m2 + m4
    Traceback (most recent call last):
      File "/snap/pycharm-professional/325/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/testProject/venv/lib/python3.10/site-packages/magnitude/magnitude.py", line 83, in __add__
        raise TypeError('Added magnitudes must have the same units.')
    TypeError: Added magnitudes must have the same units.

First, we need to define a new magnitude ``m`` as ``m1 * m2``:

.. code-block::

    m = m1 * m2
    m
    200 ± 28.284271247461906 m·m (14.142135623730953%)

Then, we need to change the unit of ``m`` from ``'m·m'`` to ``'m²'``:

.. code-block::

    m.unit = 'm²'
    m
    200 ± 28.284271247461906 m² (14.142135623730953%)

Finally we can do ``m + m4``:

.. code-block::

    m + m4
    220 ± 28.354893757515654 m² (12.888588071598026%)
