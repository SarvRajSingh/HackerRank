import re

def fun(s):
    pattern= r'^[\w|\-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    m= re.match(pattern, s)
    return m
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))
    # provide the list where m is True

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
