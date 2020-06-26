import re
def ab_match(text):
        patterns = '.*[0-9]$'
        if re.match(patterns,text):
                return 'YES'
        else:
                return 'NO'

a=input()
print(ab_match(a))
