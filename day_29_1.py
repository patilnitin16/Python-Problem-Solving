'''
You are given N phone numbers in various possible formats (they may start with 0, 91, or +91).

Your task is to write a program that:
Formats each phone number into the standard format:
+91 XXXXX XXXXX
where XXXXX XXXXX is the last 10 digits of the number (split into two groups of 5).
Sorts all the formatted phone numbers in lexicographical (dictionary) order.
Prints the sorted phone numbers, each on a new line.

📤 Output Format

Print all phone numbers in the format +91 XXXXX XXXXX, sorted lexicographically.
'''

#Code

def wrapper(f):
    def fun(l):
        newlst = []
        for i in l:
            num = i[-10:]
            newFormat = "+91 "+i[:5]+" "+i[5:]
            newlst.append(newFormat)
        f(newlst)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
