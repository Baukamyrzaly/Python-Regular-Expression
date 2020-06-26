import re
text = input()
list = re.findall(r'[ae]\w+', text)
print(list)
