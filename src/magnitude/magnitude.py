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

    Raises
    ------
    ValueError
        If the uncertainty is negative.
    """

    def __init__(self, value, uncertainty, unit, relative_uncertainty=False):
        """
        Parameters
        ----------
        value : int or float
            value of the magnitude
        uncertainty : int or float
            uncertainty of the magnitude in the units of the magnitude
        unit : str
            unit of the magnitude
        relative_uncertainty : bool, optional
            uncertainty of the magnitude in percentage units (default False)
        """
        if uncertainty < 0:
            raise ValueError('Uncertainty must be positive.')
        self.value = value
        self.unit = unit
        if relative_uncertainty:
            self.uncertainty = uncertainty * abs(value)
        else:
            self.uncertainty = uncertainty

    def relative_uncertainty(self):
        # Return the relative uncertainty
        return self.uncertainty / abs(self.value)

    def percentage_uncertainty(self):
        # Return the percentage uncertainty
        return self.relative_uncertainty() * 100

    def __repr__(self):
        value = float(self.value)
        uncertainty = float(self.uncertainty)
        percentage_uncertainty = float(self.percentage_uncertainty())
        return f'{value} \u00B1 {uncertainty} {self.unit} ({percentage_uncertainty}%)'

    def __add__(self, other):
        """Magnitudes can be summed as long as they have the same units."""
        if self.unit == other.unit:
            value = self.value + other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, uncertainty=uncertainty, unit=self.unit)
            return magnitude
        else:
            raise TypeError('Added magnitudes must have the same units.')

    def __sub__(self, other):
        """Magnitudes can be subtracted as long as they have the same units."""
        if self.unit == other.unit:
            value = self.value - other.value
            uncertainty = sqrt(self.uncertainty ** 2 + other.uncertainty ** 2)
            magnitude = Magnitude(value=value, uncertainty=uncertainty, unit=self.unit)
            return magnitude
        else:
            raise TypeError('Subtracted magnitudes must have the same units.')

    def __mul__(self, other):
        """The unit resulting from the product will be the concatenation of the individual magnitude units."""
        value = self.value * other.value
        unit = f'({self.unit})·({other.unit})'
        relative_uncertainty = sqrt(self.relative_uncertainty() ** 2 + other.relative_uncertainty() ** 2)
        magnitude = Magnitude(value=value, uncertainty=relative_uncertainty, unit=unit, relative_uncertainty=True)
        return magnitude

    def __truediv__(self, other):
        """The unit resulting from the division will be the concatenation of the individual magnitude units."""
        value = self.value / other.value
        unit = f'({self.unit})/({other.unit})'
        relative_uncertainty = sqrt(self.relative_uncertainty() ** 2 + other.relative_uncertainty() ** 2)
        magnitude = Magnitude(value=value, uncertainty=relative_uncertainty, unit=unit, relative_uncertainty=True)
        return magnitude
