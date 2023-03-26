import pytest

from src.magnitude import Magnitude


class TestMagnitudeDefinition:
    def test_absolute_uncertainty(self):
        m = Magnitude(value=100, uncertainty=1, unit='m')
        assert str(m) == '100.0 ± 1.0 m (1.0%)'

    def test_relative_uncertainty(self):
        m = Magnitude(value=100, uncertainty=0.01, unit='m', relative_uncertainty=True)
        assert str(m) == '100.0 ± 1.0 m (1.0%)'

    def test_negative_value(self):
        m1 = Magnitude(value=-100, uncertainty=1, unit='m')
        m2 = Magnitude(value=-100, uncertainty=0.01, unit='m', relative_uncertainty=True)
        assert str(m1) == '-100.0 ± 1.0 m (1.0%)'
        assert str(m2) == '-100.0 ± 1.0 m (1.0%)'

    # def test_zero_value(self):
    #     with pytest.raises(ZeroDivisionError):
    #         Magnitude(value=0, uncertainty=1, unit='m')
    #     with pytest.raises(ZeroDivisionError):
    #         Magnitude(value=0, uncertainty=0.01, unit='m', relative_uncertainty=True)

    def test_zero_uncertainty(self):
        m1 = Magnitude(value=100, uncertainty=0, unit='m')
        m2 = Magnitude(value=100, uncertainty=0, unit='m', relative_uncertainty=True)
        assert str(m1) == '100.0 ± 0.0 m (0.0%)'
        assert str(m2) == '100.0 ± 0.0 m (0.0%)'

    def test_non_dimensional(self):
        m1 = Magnitude(value=100, uncertainty=1, unit='')
        m2 = Magnitude(value=100, uncertainty=0.01, unit='', relative_uncertainty=True)
        assert str(m1) == '100.0 ± 1.0  (1.0%)'
        assert str(m2) == '100.0 ± 1.0  (1.0%)'

    def test_negative_uncertainty(self):
        with pytest.raises(ValueError) as exc:
            Magnitude(value=100, uncertainty=-1, unit='m')
        assert 'Uncertainty must be positive.' in str(exc.value)
        with pytest.raises(ValueError) as exc:
            Magnitude(value=100, uncertainty=-0.01, unit='m', relative_uncertainty=True)
        assert 'Uncertainty must be positive.' in str(exc.value)


class TestMagnitudeAttributeAssigment:
    def test_value(self):
        m = Magnitude(value=100, uncertainty=1, unit='m')
        m.value = 10
        assert str(m) == '10.0 ± 1.0 m (10.0%)'

    def test_unit(self):
        m = Magnitude(value=100, uncertainty=1, unit='m')
        m.unit = 'cm'
        assert str(m) == '100.0 ± 1.0 cm (1.0%)'

    def test_uncertainty(self):
        m = Magnitude(value=100, uncertainty=1, unit='m')
        m.uncertainty = 10
        assert str(m) == '100.0 ± 10.0 m (10.0%)'


class TestMagnitudeOperators:
    m1 = Magnitude(value=10, uncertainty=1, unit='m')
    m2 = Magnitude(value=20, uncertainty=2, unit='m')
    m3 = Magnitude(value=20, uncertainty=2, unit='cm')

    def test_sum_same_units(self):
        assert str(self.m1 + self.m2) == '30.0 ± 2.23606797749979 m (7.4535599249993%)'

    def test_sum_different_units(self):
        with pytest.raises(TypeError) as exc:
            self.m1 + self.m3
        assert 'Added magnitudes must have the same units.' in str(exc.value)

    def test_subtract_same_units(self):
        assert str(self.m2 - self.m1) == '10.0 ± 2.23606797749979 m (22.360679774997898%)'

    def test_subtract_different_units(self):
        with pytest.raises(TypeError) as exc:
            self.m1 - self.m3
        assert 'Subtracted magnitudes must have the same units.' in str(exc.value)

    def test_multiply(self):
        assert str(self.m1 * self.m2) == '200.0 ± 28.284271247461906 (m)·(m) (14.142135623730953%)'

    def test_divide(self):
        assert str(self.m2 / self.m1) == '2.0 ± 0.28284271247461906 (m)/(m) (14.142135623730953%)'
