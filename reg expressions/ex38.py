import re

a = input()
print(re.findall(r'"(.*)"', a))
