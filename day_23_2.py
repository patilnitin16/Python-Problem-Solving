'''
Input Format

One line of input: an integer N.

Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.

'''

#Code

#Optimized Code

cube = lambda x: x**3

def fibonacci(n):
    prev,curr = 0,1
    lst = []
    for i in range(n):
        lst.append(prev)
        prev,curr = curr,prev+curr
    return lst

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))