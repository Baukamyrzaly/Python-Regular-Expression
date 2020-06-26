import re
text = input()
result = re.split(r'\D+', text)
for element in result:
    print(element)
