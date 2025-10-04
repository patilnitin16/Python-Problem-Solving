'''
You are given a string s and an integer k, where k is a divisor of the length of s.
Your task is to:
Split the string into len(s) / k substrings, each of length k.
For each substring, remove duplicate characters while keeping only the first occurrence of each character.
Print the resulting substrings on separate lines.

'''

#Code 1
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        seen = set()
        out = []
        chunk = string[i:i+k]
        for ch in chunk:
            if ch not in seen:
                seen.add(ch)
                out.append(ch)
        print("".join(out))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#Code 2
def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        chunk = string[i:i+k]
        print(''.join(dict.fromkeys(chunk)))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    