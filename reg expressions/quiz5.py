import re
def ab_match(text):
        patterns = 'ab{3}?'
        if re.search(patterns,text):
                return 'YES'
        else:
                return 'NO'

a=input()
print(ab_match(a))
