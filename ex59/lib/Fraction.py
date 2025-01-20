class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def add(self, other):
        tu3 = self.numerator*other.denominator + other.numerator*self.denominator
        mau3 = self.denominator*other.denominator
        return Fraction(tu3, mau3)
    def subtract(self, other):
        tu3 = self.numerator*other.denominator - other.numerator*self.denominator
        mau3 = self.denominator*other.denominator
        return Fraction(tu3, mau3)
    def times(self, other):
        tu3 = self.numerator * other.numerator
        mau3 = self.denominator * other.denominator
        return Fraction(tu3, mau3)
    def divide(self, other):
        tu3 = self.numerator*other.denominator
        mau3 = self.denominator*other.numerator
        return Fraction(tu3, mau3)