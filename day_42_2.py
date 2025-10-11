'''
Write a Python program that takes several fractions as input, multiplies them together, and prints the numerator and denominator of the resulting product in their simplified form.

Task Description:
You are given N fractions.
Your task is to calculate the product of all fractions.
Then, print the numerator and denominator of the simplified result.
'''

#code

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x,y:x*y,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)