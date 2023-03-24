import pytest

from src.magnitude import Magnitude


class TestMagnitudeDefinition:
    def test_absolute_uncertainty(self):
        m = Magnitude(value=20, unit='m', uncertainty=2)
        assert str(m) == '20 ± 2 m (10.0%)'

    def test_relative_uncertainty(self):
        m = Magnitude(value=20, unit='m', relative_uncertainty=0.1)
        assert str(m) == '20 ± 2.0 m (10.0%)'

    def test_matching_uncertainties(self):
        m = Magnitude(value=20, unit='m', uncertainty=2, relative_uncertainty=0.1)
        assert str(m) == '20 ± 2 m (10.0%)'

    def test_no_matching_uncertainties(self):
        with pytest.raises(ValueError) as exc:
            Magnitude(value=20, unit='m', uncertainty=3, relative_uncertainty=0.1)
        assert 'Absolute and relative uncertainties do not match.' in str(exc.value)

    def test_zero_uncertainty(self):
        m1 = Magnitude(value=20, unit='m', uncertainty=0)
        m2 = Magnitude(value=20, unit='m', relative_uncertainty=0)
        m3 = Magnitude(value=20, unit='m', uncertainty=0, relative_uncertainty=0)
        assert str(m1) == '20 ± 0 m (0.0%)'
        assert str(m2) == '20 ± 0 m (0%)'
        assert str(m3) == '20 ± 0 m (0%)'

    def test_non_dimensional(self):
        m = Magnitude(value=20, unit='', uncertainty=2)
        assert str(m) == '20 ± 2  (10.0%)'

    def test_no_uncertainties(self):
        with pytest.raises(TypeError) as exc:
            Magnitude(value=20, unit='m')
        assert 'Magnitudes must have uncertainties.' in str(exc.value)

    def test_negative_uncertainty(self):
        with pytest.raises(ValueError) as exc:
            Magnitude(value=20, unit='m', uncertainty=-2)
        assert 'Uncertainties must be positive.' in str(exc.value)
        with pytest.raises(ValueError) as exc:
            Magnitude(value=20, unit='m', relative_uncertainty=-0.1)
        assert 'Uncertainties must be positive.' in str(exc.value)
        with pytest.raises(ValueError) as exc:
            Magnitude(value=20, unit='m', uncertainty=-2, relative_uncertainty=-0.1)
        assert 'Uncertainties must be positive.' in str(exc.value)

    def test_zero_value(self):
        with pytest.warns(UserWarning):
            m = Magnitude(value=0, unit='m', uncertainty=0.1)
            assert str(m) == '0 ± 0.1 m (inf%)'
        with pytest.warns(UserWarning):
            m = Magnitude(value=0, unit='m', relative_uncertainty=0.1)
            assert str(m) == '0 ± 0.0 m (10.0%)'


class TestMagnitudeOperators:
    m1 = Magnitude(value=10, unit='m', uncertainty=1)
    m2 = Magnitude(value=20, unit='m', uncertainty=2)
    m3 = Magnitude(value=20, unit='cm', uncertainty=2)

    def test_sum_same_units(self):
        assert str(self.m1 + self.m2) == '30 ± 2.23606797749979 m (7.4535599249993%)'

    def test_sum_different_units(self):
        with pytest.raises(TypeError) as exc:
            self.m1 + self.m3
        assert 'Added magnitudes must have the same units.' in str(exc.value)

    def test_subtract_same_units(self):
        assert str(self.m2 - self.m1) == '10 ± 2.23606797749979 m (22.360679774997898%)'

    def test_subtract_different_units(self):
        with pytest.raises(TypeError) as exc:
            self.m1 - self.m3
        assert 'Subtracted magnitudes must have the same units.' in str(exc.value)

    def test_multiply(self):
        assert str(self.m1 * self.m2) == '200 ± 28.284271247461906 (m)·(m) (14.142135623730953%)'

    def test_divide(self):
        assert str(self.m2 / self.m1) == '2.0 ± 0.28284271247461906 (m)/(m) (14.142135623730953%)'
