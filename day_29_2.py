'''
You are given the details of N people, where each person’s details consist of:
FirstName LastName Age Gender
FirstName → a string
LastName → a string
Age → an integer
Gender → "M" for male or "F" for female
Your task is to:
Sort the people in ascending order of their age.
Format their names using the following rules:
If the gender is "M", the name should be prefixed with "Mr. "
If the gender is "F", the name should be prefixed with "Ms. "
The output format should be:
Title FirstName LastName
'''

#Code

import operator
def person_lister(f):
    def inner(people):
        new_data = sorted(people,key=lambda x : int(x[2]))
        for i in new_data:
            return map(f,new_data)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')