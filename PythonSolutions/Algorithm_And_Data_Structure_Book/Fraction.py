from math import gcd


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __add__(self, other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __sub__(self, other):
        new_num = (self.num * other.den) - (self.den * other.num)
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        common = gcd(new_num, new_den)
        return Fraction(new_num//common, new_den//common)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other):
        new_self_num = self.num * other.den
        new_other_num = other.num * self.den
        return new_self_num > new_other_num

    def __lt__(self, other):
        new_self_num = self.num * other.den
        new_other_num = other.num * self.den
        return new_self_num < new_other_num

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)


fraction_one = Fraction(4, 6)
fraction_two = Fraction(5, 12)

print(fraction_one)
print(fraction_two)

fraction_add = fraction_one + fraction_two
print(fraction_add)

fraction_sub = fraction_one - fraction_two
print(fraction_sub)

fraction_mul = fraction_one * fraction_two
print(fraction_mul)

fraction_div = fraction_one / fraction_two
print(fraction_div)

fraction_gt = fraction_one > fraction_two
print(fraction_gt)

fraction_lt = fraction_one < fraction_two
print(fraction_lt)

print([fraction_one, fraction_two])
