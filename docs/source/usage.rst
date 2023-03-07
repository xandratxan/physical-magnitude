User guide
==========

Installation
------------

Defining a magnitude
--------------------

How magnitudes can be defined

Magnitudes are defined as instantiations of the class ``Magnitude``.

.. code-block::

   from magnitude.magnitude import Magnitude

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
      File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
        self.complete_uncertainties()
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 60, in complete_uncertainties
        raise ValueError('Absolute and relative uncertainties do not match.')
    ValueError: Absolute and relative uncertainties do not match.

Magnitudes without uncertainties may be defined with zero uncertainty.

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=0)
    20 ± 0 m (0.0%)

.. code-block::

    Magnitude(value=20, unit='m', relative_uncertainty=0)
    20 ± 0 m (0%)

.. code-block::

    Magnitude(value=20, unit='m', uncertainty=0, relative_uncertainty=0)
    20 ± 0 m (0%)

How magnitudes cannot be defined

Magnitudes must have uncertainties. They cannot be defined with no uncertainties:

.. code-block::

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

Magnitudes cannot be defined with negative uncertainties, since it have no physical meaning:

.. code-block::

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

.. code-block::

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

Magnitudes with exact value of zero cannot be defined, since relative uncertainty would be infinite.

.. code-block::

    Magnitude(value=0, unit='m', uncertainty=0.1)
    Traceback (most recent call last):
      File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 10, in __init__
        self.complete_uncertainties()
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 63, in complete_uncertainties
        self.relative_uncertainty = self.uncertainty / self.value
    ZeroDivisionError: float division by zero

.. code-block::

    Magnitude(value=0, unit='m', relative_uncertainty=0.1)
    0 ± 0.0 m (10.0%)

Simple operations with magnitudes
---------------------------------

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
      File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 22, in __add__
        raise TypeError('Added magnitudes must have the same units.')
    TypeError: Added magnitudes must have the same units.

.. code-block::

    m2 - m3
    Traceback (most recent call last):
      File "/snap/pycharm-professional/319/plugins/python/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "/home/txan/PycharmProjects/magnitudes/magnitude/magnitude.py", line 31, in __sub__
        raise TypeError('Subtracted magnitudes must have the same units.')
    TypeError: Subtracted magnitudes must have the same units.

Magnitudes can be multiplied or divided independently of their units.
The unit resulting from the product or the division will be the concatenation of the individual magnitudes:

.. code-block::

    m1 * m2
    200 ± 28.284271247461906 m·m (14.142135623730953%)

.. code-block::

    m2 / m1
    2.0 ± 0.28284271247461906 m/m (14.142135623730953%)
