"""
Module to perform simple operations with magnitudes including units and uncertainties.

Classes
-------
Magnitude :
    Class to perform simple operations with magnitudes including units and uncertainties.
"""
from math import sqrt
from warnings import warn


class Magnitude:
    """
    Class to perform simple operations with magnitudes including units and uncertainties.

    It allows to define magnitudes with value, uncertainty and unit.
    It allows to compute simple operations providing the result for the magnitude value, uncertainty and unit.
    Available operations include summation, subtraction, multiplication and division.

    Magnitudes must have value, uncertainty and unit.
    If absolute uncertainty is provided, relative uncertainty will be calculated, and vice versa.
    If both uncertainties are provided, the agreement between values will be checked.
    Magnitudes without uncertainties can be defined with zero uncertainty.
    Magnitudes with zero value can be defined, but should be handled with care,
    since uncertainties may not have physical meaning.

    Magnitudes can be summed or subtracted as long as they have the same units.
    Magnitudes can be multiplied or divided independently of their units.
    The unit of the product or division is the concatenation of the units of the individual magnitude.

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

    Raises
    ------
    ValueError
        If the value of absolute and relative uncertainties do not match.
    TypeError
        If the magnitude does not have absolute or relative uncertainty defined.
    ValueError
        If the absolute or relative uncertainty are negative.
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
        return f'{self.value} \u00B1 {self.uncertainty} {self.unit} ({self.relative_uncertainty * 100}%)'

    def __add__(self, other):
        """Magnitudes can be summed as long as they have the same units."""
        if self.unit == other.unit:
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
        unit = f'({self.unit})·({other.unit})'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def __truediv__(self, other):
        """The unit resulting from the division will be the concatenation of the individual magnitude units."""
        value = self.value / other.value
        unit = f'({self.unit})/({other.unit})'
        relative_uncertainty = sqrt(self.relative_uncertainty ** 2 + other.relative_uncertainty ** 2)
        magnitude = Magnitude(value=value, unit=unit, relative_uncertainty=relative_uncertainty)
        return magnitude

    def _magnitude_consistency_check(self):
        """
        Check the consistency of the magnitude definition.

        Magnitudes must have value, uncertainty and unit.
        If absolute uncertainty is provided, relative uncertainty will be calculated, and vice versa.
        If both uncertainties are provided, the agreement between values will be checked.
        Magnitudes without uncertainties can be defined with zero uncertainty.
        Magnitudes with zero value can be defined, but should be handled with care,
        since uncertainties may not have physical meaning.

        Raises
        ------
        ValueError
            If the value of absolute and relative uncertainties do not match.
        TypeError
            If the magnitude does not have absolute or relative uncertainty defined.
        ValueError
            If the absolute or relative uncertainty are negative.
        """
        if self.uncertainty is not None:
            if self.relative_uncertainty is not None:
                if self.relative_uncertainty != self.uncertainty / self.value:
                    raise ValueError('Absolute and relative uncertainties do not match.')
            else:
                if self.value == 0:
                    warn('Magnitude defined with zero value. Uncertainties may not have physical meaning.')
                    self.relative_uncertainty = float('inf')
                else:
                    self.relative_uncertainty = self.uncertainty / self.value
        else:
            if self.relative_uncertainty is not None:
                if self.value == 0:
                    warn('Magnitude defined with zero value. Uncertainties may not have physical meaning.')
                self.uncertainty = self.value * self.relative_uncertainty
            else:
                raise TypeError('Magnitudes must have uncertainties.')
        if self.uncertainty < 0 or self.relative_uncertainty < 0:
            raise ValueError('Uncertainties must be positive.')
