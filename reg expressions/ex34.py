import re
text = input()
print(re.findall(r"\b\w{3,5}\b", text))
