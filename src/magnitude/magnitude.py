"""
Module to perform simple operations with magnitudes including units and uncertainties.

Classes
-------
Magnitude :
    Class to perform simple operations with magnitudes including units and uncertainties.
"""
from math import sqrt


class Magnitude:
    """
    Class to perform simple operations with magnitudes including units and uncertainties.

    It allows to define magnitudes with value, uncertainty and unit.
    It allows to compute simple operations providing the result for the magnitude value, uncertainty and unit.
    Available operations include summation, subtraction, multiplication and division.

    Attributes
    ----------
    value : int or float
        value of the magnitude
    unit : str
        unit of the magnitude
    uncertainty : int or float
        uncertainty of the magnitude in the units of te magnitude (default None)
    relative_uncertainty : int or float
        uncertainty of the magnitude in percentage units (default None)
    """

    def __init__(self, value, unit, uncertainty=None, relative_uncertainty=None):
        """
        Parameters
        ----------
        value : int or float
            value of the magnitude
        unit : str
            unit of the magnitude
        uncertainty : int or float, optional
            uncertainty of the magnitude in the units of te magnitude (default None)
        relative_uncertainty : int or float, optional
            uncertainty of the magnitude in percentage units (default None)
        """
        self.value = value
        self.unit = unit
        self.uncertainty = uncertainty
        self.relative_uncertainty = relative_uncertainty
        self._magnitude_consistency_check()

    def __repr__(self):
        return f'Magnitude(value={self.value}, unit={self.unit},' \
               f'uncertainty={self.uncertainty}, relative_uncertainty={self.relative_uncertainty})'

    def __str__(self):
        return f'{self.value} \u00B1 {self.uncertainty} {self.unit} ({self.relative_uncertainty * 100}%)'

    def __add__(self, other):
        if self.unit == other.unit:
            """Magnitudes can be summed as long as they have the same units."""
            value = self.value + other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, unit=self.unit, uncertainty=uncertainty)
            return magnitude
        else:
            raise TypeError('Added magnitudes must have the same units.')

    def __sub__(self, other):
        """Magnitudes can be subtracted as long as they have the same units."""
        if self.unit == other.unit:
            value = self.value - other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, unit=self.unit, uncertainty=uncertainty)
            return magnitude
        else:
            raise TypeError('Subtracted magnitudes must have the same units.')

    def __mul__(self, other):
        """The unit resulting from the product will be the concatenation of the individual magnitude units."""
        value = self.value * other.value
        unit = f'{self.unit}·{other.unit}'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def __truediv__(self, other):
        """The unit resulting from the division will be the concatenation of the individual magnitude units."""
        value = self.value / other.value
        unit = f'{self.unit}/{other.unit}'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def _magnitude_consistency_check(self):
        """
        Check the consistency of the magnitude definition.

        Magnitudes must have value, uncertainty and unit.
        If absolute uncertainty is provided, relative uncertainty will be calculated, and vice versa.
        If both uncertainties are provided, the agreement between values will be checked.
        Magnitudes without uncertainties may be defined with zero uncertainty.

        Raises
        ------
        ValueError
            If the value of absolute and relative uncertainties do not match.
        TypeError
            If the magnitude does not have absolute or relative uncertainty defined.
        ValueError
            If the absolute or relative uncertainty are negative.
        """
        # TODO: magnitudes with value zero and uncertainty cannot be defined, but they can with relative uncertainty.
        if self.uncertainty is not None:
            if self.relative_uncertainty is not None:
                if self.relative_uncertainty != self.uncertainty / self.value:
                    raise ValueError('Absolute and relative uncertainties do not match.')
            else:
                self.relative_uncertainty = self.uncertainty / self.value
        else:
            if self.relative_uncertainty is not None:
                self.uncertainty = self.value * self.relative_uncertainty
            else:
                raise TypeError('Magnitudes must have uncertainties.')
        if self.uncertainty < 0 or self.relative_uncertainty < 0:
            raise ValueError('Uncertainties must be positive.')
