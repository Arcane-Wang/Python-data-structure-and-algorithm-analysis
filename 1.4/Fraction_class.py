class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num


def gcd(m, n):
    while m % n:
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


a, b = Fraction(54, 23), Fraction(89, 2)
print(a)
print(a+b)
