import re
def ab_match(text):
        patterns = '^[A-Z][a-z]'
        if re.search(patterns,text):
                return 'YES'
        else:
                return 'NO'
a=input()
print(ab_match(a))

