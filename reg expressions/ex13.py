import re
def ab_match(text):
        patterns = r'z\w*z*'
        if not re.search(patterns,text):
                return 'YES'
        else:
                return 'NO'
a=input()
print(ab_match(a))  
