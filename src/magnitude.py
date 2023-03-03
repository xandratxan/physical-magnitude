from math import sqrt


class Magnitude:
    def __init__(self, value, unit, uncertainty=None, relative_uncertainty=None):
        self.value = value
        self.unit = unit
        self.uncertainty = uncertainty
        self.relative_uncertainty = relative_uncertainty
        self.complete_uncertainties()

    def __repr__(self):
        return f'{self.value} \u00B1 {self.uncertainty} {self.unit} ({self.relative_uncertainty * 100}%)'

    def __add__(self, other):
        if self.unit == other.unit:
            value = self.value + other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, unit=self.unit, uncertainty=uncertainty)
            return magnitude
        else:
            raise TypeError('Added magnitudes must have the same units.')

    def __sub__(self, other):
        if self.unit == other.unit:
            value = self.value - other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, unit=self.unit, uncertainty=uncertainty)
            return magnitude
        else:
            raise TypeError('Subtracted magnitudes must have the same units.')

    def __mul__(self, other):
        value = self.value * other.value
        unit = f'{self.unit}·{other.unit}'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def __truediv__(self, other):
        # IMPORTANT: as magnitudes with value zero cannot be defined, this method will never raise a ZeroDivisionError
        # exception.
        value = self.value / other.value
        unit = f'{self.unit}/{other.unit}'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def complete_uncertainties(self):
        # Magnitudes must have value, uncertainty and unit.
        # TODO Magnitudes without uncertainties may be defined with zero uncertainty.
        # If absolute uncertainty is provided, relative uncertainty will be calculated, and vice versa.
        # If both uncertainties are provided, the agreement between values will be checked.
        # IMPORTANT: magnitudes with value zero cannot be defined: relative uncertainty would be infinite and a
        # ZeroDivisionError exception would be raised.
        if self.uncertainty:
            if self.relative_uncertainty:
                # if uncertainty=X, relative_uncertainty=X: check good agreement between uncertainties
                if self.relative_uncertainty != self.uncertainty / self.value:
                    raise ValueError('Absolute and relative uncertainties do not match.')
            else:
                # if uncertainty=X, relative_uncertainty=None: compute relative uncertainty
                self.relative_uncertainty = self.uncertainty / self.value
        else:
            if self.relative_uncertainty:
                # if uncertainty=None, relative_uncertainty=X: compute absolute uncertainty
                self.uncertainty = self.value * self.relative_uncertainty
            else:
                # if uncertainty=None, relative_uncertainty=None: ?
                raise TypeError('Magnitudes must have uncertainties.')
        if self.uncertainty < 0 or self.relative_uncertainty < 0:
            raise ValueError('Uncertainties must be positive.')
