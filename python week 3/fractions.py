class Fraction:
    """This class represents fractions
    """
    def __init__(self, nume, denom):
        """Initializes numerator and denominator

        Args:
            nume(int): the numerator
            denom(int): the denominator
        """
        self.nume = nume
        if denom == 0:
            raise ValueError("Denominator cannot be zero.")
        self.denom = denom

    def __str__(self):
        return f'{self.nume}/{self.denom}'

    def __add__(self, other):
        if type(other) is Fraction:
            if self.denom == other.denom:
                return Fraction(self.nume + other.nume, self.denom)
            else:
                if self.denom < other.denom:
                    diff = other.denom // self.denom
                    newn = self.nume * diff
                    return Fraction(newn + other.nume, other.denom)
                if other.denom < self.denom:
                    diff2 = self.denom // other.denom
                    newn2 = other.nume * diff2
                    return Fraction(newn2 + self.nume, self.denom)
        elif type(other) is int:
            return Fraction((self.denom * other) + self.nume, self.denom)
        else:
            raise TypeError("Type is not supported.")

    def __sub__(self, other):
        if type(other) is Fraction:
            if self.denom == other.denom:
                return Fraction(self.nume - other.nume, self.denom)
            else:
                if self.denom < other.denom:
                    diff = other.denom // self.denom
                    newn = self.nume * diff
                    return Fraction(newn - other.nume, other.denom)
                if other.denom < self.denom:
                    diff2 = self.denom // other.denom
                    newn2 = other.nume * diff2
                    return Fraction(newn2 - self.nume, self.denom)
        elif type(other) is int:
            return Fraction(self.nume - other, self.denom)
        else:
            raise TypeError("Type is not supported.")

    def __mul__(self, other):
        if type(other) is Fraction:
            return Fraction(self.nume * other.nume, self.denom * other.denom)
        else:
            raise TypeError("Type is not supported.")

    def __eq__(self, other):
        if type(other) is Fraction:
            if self.denom == other.denom:
                return (self.nume == other.nume) and (self.denom == other.denom)
            else:
                if self.denom < other.denom:
                    diff = other.denom // self.denom
                    newn = self.nume * diff
                    newd = self.denom * diff
                    return (newn == other.nume) and (newd == other.denom)
                if other.denom < self.denom:
                    diff2 = self.denom // other.denom
                    newn2 = other.nume * diff2
                    newd2 = other.denom * diff2
                    return (newn2 == self.nume) and (newd2 == other.denom)
        else:
            raise TypeError("Type is not supported.")
