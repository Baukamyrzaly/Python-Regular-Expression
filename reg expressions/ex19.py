import re
patterns = [ 'Fox', 'Dog', 'Horse' ]
text = 'the quick brown fox jumps over the lazy dog.'
for pattern in patterns:
    print (pattern, text)
    if re.search(pattern,  text):
        print('YES')
    else:
        print('NO')
