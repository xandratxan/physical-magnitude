import pytest

import src.magnitude as mag


def test_define_magnitude_with_absolute_uncertainty():
    m = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m) == '20 ± 2 m (0.1%)'


def test_define_magnitude_with_relative_uncertainty():
    m = mag.Magnitude(value=20, unit='m', relative_uncertainty=0.1)
    assert str(m) == '20 ± 2.0 m (0.1%)'


def test_define_magnitude_with_matching_uncertainties():
    m = mag.Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
    assert str(m) == '20 ± 2 m (0.1%)'


def test_define_magnitude_with_no_matching_uncertainties():
    with pytest.raises(ValueError) as exc:
        mag.Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
    assert 'Absolute and relative uncertainties do not match.' in str(exc.value)


def test_define_magnitude_with_no_uncertainty():
    with pytest.raises(TypeError) as exc:
        mag.Magnitude(value=20, unit='m')
    assert 'Magnitudes must have uncertainties.' in str(exc.value)
