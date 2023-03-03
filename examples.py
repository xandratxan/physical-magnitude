import src.magnitude as mag

# if uncertainty=X, relative_uncertainty=None: compute relative uncertainty
m1 = mag.Magnitude(value=20, unit='m', uncertainty=2)
print(m1)

# if uncertainty=None, relative_uncertainty=X: compute absolute uncertainty
m2 = mag.Magnitude(value=30, unit='m', relative_uncertainty=0.1)
print(m2)

# if uncertainty=X, relative_uncertainty=X: check good agreement between uncertainties
m3 = mag.Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
print(m3)
try:
    m4 = mag.Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
except ValueError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')

# if uncertainty=None, relative_uncertainty=None: raise exception
try:
    m5 = mag.Magnitude(value=10, unit='m')
except TypeError as exc:
    print(f'Raised {type(exc).__name__}: {exc}')
