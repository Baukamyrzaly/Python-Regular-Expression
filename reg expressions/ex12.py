import re
def ab_match(text):
        patterns = r'\w*z.\w*'
        if re.search(patterns,text):
                return 'YES'
        else:
                return 'NO'
a=input()
print(ab_match(a))  
