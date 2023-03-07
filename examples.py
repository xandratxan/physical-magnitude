from magnitude.magnitude import Magnitude

# Defining a magnitude

# How magnitudes can be defined

# Magnitudes are defined as instantiations of the class ``Magnitude``.
# Magnitudes must have value, uncertainty and unit.
# If absolute uncertainty is provided, relative uncertainty will be calculated:
m = Magnitude(value=20, unit='m', uncertainty=2)
print(m)
# If relative uncertainty is provided, absolute uncertainty will be calculated:
m = Magnitude(value=30, unit='m', relative_uncertainty=0.1)
print(m)
# If both uncertainties are provided, the agreement between values will be checked.
# If both uncertainties are equivalent, the magnitude will be defined correctly:
m = Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
print(m)
# If both uncertainties are not equivalent, an exception will be raised:
try:
    m = Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
except ValueError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
# Magnitudes without uncertainties may be defined with zero uncertainty.
m = Magnitude(value=20, unit='m', uncertainty=0)
print(m)
m = Magnitude(value=20, unit='m', relative_uncertainty=0)
print(m)
# Magnitudes defined with zero value may be tricky: uncertainties may not have physical meaning:
m = Magnitude(value=0, unit='m', uncertainty=0.1)
print(m)
m = Magnitude(value=0, unit='m', relative_uncertainty=0.1)
print(m)

# How magnitudes cannot be defined

# Magnitudes must have uncertainties. They cannot be defined with no uncertainties:
try:
    m = Magnitude(value=10, unit='m')
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
# Magnitudes cannot be defined with negative uncertainties, since it have no physical meaning:
try:
    m = Magnitude(value=20, unit='m', uncertainty=-2)
except ValueError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
try:
    m = Magnitude(value=30, unit='m', relative_uncertainty=-0.1)
except ValueError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
# Magnitudes with exact value of zero cannot be defined, since relative uncertainty would be infinite.
m = Magnitude(value=0, unit='m', uncertainty=0.1)
print(m)
Magnitude(value=0, unit='m', relative_uncertainty=0.1)
print(m)

# Simple operations with magnitudes

# First, define some magnitudes to operate with them:
m1 = Magnitude(value=10, unit='m', uncertainty=1)
m2 = Magnitude(value=20, unit='m', uncertainty=2)
m3 = Magnitude(value=20, unit='cm', uncertainty=2)
# Magnitudes can be summed or subtracted as long as they have the same units:
print(m1 + m2)
print(m2 - m1)
# If they have different units, an exception will be raised:
try:
    print(m1 + m3)
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
try:
    print(m2 - m3)
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
# Magnitudes can be multiplied or divided independently of their units.
# The unit resulting from the product or the division will be the concatenation of the individual magnitudes:
print(m1 * m2)
print(m2 / m1)

# TODO: Test concatenation of operations
