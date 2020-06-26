import re
def azAZ09(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

a=input()
print (azAZ09(a))
