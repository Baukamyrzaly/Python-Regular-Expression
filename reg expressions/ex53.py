import re
str1 = input()
lower_remove = lambda text: re.sub('[a-z]', '', text)
result =  lower_remove(str1)
print(result)
