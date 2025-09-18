'''
Print an Alphabet Rangoli pattern of size N.

🔹 The Rangoli should have the following properties:

It is made up of English lowercase alphabets.

The center of the Rangoli has the letter 'a'.

The boundary has the Nth alphabet (for size = 3, boundary is 'c').

All letters are separated by '-'.

The width of each row = 4*N - 3.

'''

#Code

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    width = 4*size - 3   # total width
    
    for i in range(size-1, -size, -1):
        row = alpha[size-1:abs(i):-1] + alpha[abs(i):size]
        print("-".join(row).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    

