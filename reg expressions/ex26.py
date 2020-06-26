import re
words = input()
for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            print(m.groups())
