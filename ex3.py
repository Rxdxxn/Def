a=int(input('Dati numaratorul 1 fractiei:'))
b=int(input('Dati numitorul 1 fractiei:'))
c=int(input('Dati numaratorul 2 fractiei:'))
d=int(input('Dati numitorul 2 fractiei:'))
from fractions import Fraction
def af():
    s=Fraction(a,b)+Fraction(c,d)
    return s
def pf():
    p=Fraction(a,b) * Fraction(c,d)
    return p
print('Suma=', af())
print('Produsul=', pf())