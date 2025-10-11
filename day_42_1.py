'''
Write a Python program to validate and sort email addresses based on specific rules.
Task: You are given a list of email addresses.
You must filter out invalid emails and print only the valid ones in sorted order.
An email address is valid if it meets all these conditions:
It must be in the format username@websitename.extension
The username:can only contain letters, digits, underscores (_), and hyphens (-)
The websitename:can only contain letters and digits
The extension:can only contain letters
must be 3 characters or fewer
'''
#Code
def fun(s):
    if s.count("@") != 1:
        return False
    username,rest = s.split("@")
    if "." not in rest:
        return False
    if len(username) < 1:
        return False
    if not all(ch.isalnum() or ch in ["_","-"] for ch in username):
        return False
    company,extension = rest.split(".")
    if not company.isalnum():
        return False
    if not(extension.isalpha() and len(extension) <= 3):
        return False
    return True        
def filter_mail(emails):
    return list(filter(fun, emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)