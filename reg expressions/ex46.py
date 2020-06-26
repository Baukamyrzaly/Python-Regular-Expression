import re
text = input()
for a in re.finditer(r"\w+ly", text):
    print (a.start(), a.end(), a.group(0))
