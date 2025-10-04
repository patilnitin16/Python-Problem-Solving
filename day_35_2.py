'''
Kevin and Stuart are playing a game with a string. The rules of the game are:
1.Kevin scores points for every substring that starts with a vowel (A, E, I, O, U).
2.Stuart scores points for every substring that starts with a consonant.
3.The score of a substring is the number of times it occurs as a starting substring in the string.
Task:
Write a Python program that:
Takes a string as input.
Calculates the scores of Kevin and Stuart.
Prints the winner and their score in the format:
Kevin <score> if Kevin wins
Stuart <score> if Stuart wins
Draw if both scores are equal
'''

#Code
def minion_game(string):
    scoreKevin = 0
    scoreStuart = 0
    vowels = "aeiouAEIOU"
    for i in range(len(string)):
        if string[i] in vowels:
            scoreKevin+= len(string)-i
        if string[i] not in vowels:
            scoreStuart+= len(string)-i  
    if(scoreKevin > scoreStuart):
        print(f"Kevin {scoreKevin}")
    elif(scoreKevin == scoreStuart):
        print("Draw")
    else:
        print(f"Stuart {scoreStuart}") 
if __name__ == '__main__':
    s = input()
    minion_game(s)    
