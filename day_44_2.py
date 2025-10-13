'''
Write a Python program that assigns a score to a list of words based on the number of vowels in each word.

Rules:
A vowel is defined as one of the following letters: 'a', 'e', 'i', 'o', 'u', 'y'.
For each word:
Count the number of vowels.
If the number of vowels is even, add 2 points to the total score.
If the number of vowels is odd, add 1 point to the total score.
Finally, print the total score of all words.
'''

#Code

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score+=1
    return score


n = int(input())
words = input().split()
print(score_words(words))