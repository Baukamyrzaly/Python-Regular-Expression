import re
pattern = 'exercises'
text = 'Python exercises, PHP exercises, C# exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(s, e)

