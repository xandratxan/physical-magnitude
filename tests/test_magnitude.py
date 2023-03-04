import pytest

import src.magnitude as mag


def test_define_magnitude_with_absolute_uncertainty():
    m = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m) == '20 ± 2 m (10.0%)'


def test_define_magnitude_with_relative_uncertainty():
    m = mag.Magnitude(value=20, unit='m', relative_uncertainty=0.1)
    assert str(m) == '20 ± 2.0 m (10.0%)'


def test_define_magnitude_with_matching_uncertainties():
    m = mag.Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
    assert str(m) == '20 ± 2 m (10.0%)'


def test_define_magnitude_with_no_matching_uncertainties():
    with pytest.raises(ValueError) as exc:
        mag.Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
    assert 'Absolute and relative uncertainties do not match.' in str(exc.value)


def test_define_magnitude_with_no_uncertainty():
    with pytest.raises(TypeError) as exc:
        mag.Magnitude(value=20, unit='m')
    assert 'Magnitudes must have uncertainties.' in str(exc.value)


def test_define_magnitude_with_negative_uncertainty():
    with pytest.raises(ValueError) as exc:
        mag.Magnitude(value=20, unit='m', uncertainty=-2)
    assert 'Uncertainties must be positive.' in str(exc.value)


def test_define_magnitude_with_negative_relative_uncertainty():
    with pytest.raises(ValueError) as exc:
        mag.Magnitude(value=30, unit='m', relative_uncertainty=-0.1)
    assert 'Uncertainties must be positive.' in str(exc.value)


def test_define_magnitude_with_zero_uncertainty():
    m = mag.Magnitude(value=20, unit='m', uncertainty=0)
    assert str(m) == '20 ± 0 m (0.0%)'


def test_define_magnitude_with_zero_relative_uncertainty():
    m = mag.Magnitude(value=20, unit='m', relative_uncertainty=0)
    assert str(m) == '20 ± 0 m (0%)'


def test_sum_magnitudes_same_units():
    m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
    m2 = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m1 + m2) == '30 ± 2.23606797749979 m (7.4535599249993%)'


def test_sum_magnitudes_different_units():
    with pytest.raises(TypeError) as exc:
        m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
        m2 = mag.Magnitude(value=20, unit='cm', uncertainty=2)
        m1 + m2
    assert 'Added magnitudes must have the same units.' in str(exc.value)


def test_subtract_magnitudes_same_units():
    m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
    m2 = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m2 - m1) == '10 ± 2.23606797749979 m (22.360679774997898%)'


def test_subtract_magnitudes_different_units():
    with pytest.raises(TypeError) as exc:
        m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
        m2 = mag.Magnitude(value=20, unit='cm', uncertainty=2)
        m1 - m2
    assert 'Subtracted magnitudes must have the same units.' in str(exc.value)


def test_multiply_magnitudes():
    m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
    m2 = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m1 * m2) == '200 ± 28.284271247461906 m·m (14.142135623730953%)'


def test_divide_magnitudes():
    m1 = mag.Magnitude(value=10, unit='m', uncertainty=1)
    m2 = mag.Magnitude(value=20, unit='m', uncertainty=2)
    assert str(m2 / m1) == '2.0 ± 0.28284271247461906 m/m (14.142135623730953%)'
