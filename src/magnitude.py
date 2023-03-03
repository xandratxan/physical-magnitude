class Magnitude:
    def __init__(self, value, unit, uncertainty=None, relative_uncertainty=None):
        self.value = value
        self.unit = unit
        self.uncertainty = uncertainty
        self.relative_uncertainty = relative_uncertainty
        self.complete_uncertainties()

    def __repr__(self):
        return f'{self.value} \u00B1 {self.uncertainty} {self.unit} ({self.relative_uncertainty}%)'

    def complete_uncertainties(self):
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
