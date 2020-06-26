import re
def ab_match(text):
        patterns = r'^[a-zA-Z0-9_]*$'
        if re.search(patterns,text):
                return 'YES'
        else:
                return 'NO'
a=input()
print(ab_match(a))  
