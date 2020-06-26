import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(s, e)




