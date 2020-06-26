import re
results = re.finditer(r"([0-9]{1,3})", "I have 1 dog, 2 cats, 4 rabbits and 12 hours in one day to spending for stady PYTHON4")

for n in results:
     print(n.group(0))
