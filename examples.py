import src.magnitude as mag

# Magnitudes definition

# if uncertainty=X, relative_uncertainty=None: compute relative uncertainty
m = mag.Magnitude(value=20, unit='m', uncertainty=2)
print(m)

# if uncertainty=None, relative_uncertainty=X: compute absolute uncertainty
m = mag.Magnitude(value=30, unit='m', relative_uncertainty=0.1)
print(m)

# if uncertainty=X, relative_uncertainty=X: check good agreement between uncertainties
m = mag.Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
print(m)
try:
    m = mag.Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
except ValueError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')

# if uncertainty=None, relative_uncertainty=None: raise exception
try:
    m = mag.Magnitude(value=10, unit='m')
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')

# Sum of magnitudes with the same or different units
m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
m2 = mag.Magnitude(value=20, unit='m', uncertainty=2)
m3 = mag.Magnitude(value=20, unit='cm', uncertainty=2)
print(m1 + m2)
try:
    print(m1 + m3)
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
