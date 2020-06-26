import re
text = input()
print(re.findall(r"\b\w{4,}\b", text))
