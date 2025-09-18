'''
Problem Statement

Given an integer n, print the following values for each integer i from 1 to n:

Decimal

Octal

Hexadecimal (capitalized)

Prints

The four values must be printed on a single line in the order specified above for each i from 1 to number.
Each value should be space-padded to match the width of the binary value of number, and the values should be separated by a single space.

'''

#Code

def print_formatted(number):
    width = len(bin(number))-2
    for i in range(1,number+1):
        print(f"{str(i).rjust(width)} {oct(i)[2:].rjust(width)} {(hex(i)[2:].upper()).rjust(width)} {bin(i)[2:].rjust(width)}")
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)