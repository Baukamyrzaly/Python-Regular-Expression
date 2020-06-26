import re

a = input()
pattern = re.compile('[\W_]+')
print(pattern.sub('', a))
