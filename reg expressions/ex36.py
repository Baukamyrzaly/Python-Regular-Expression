import re


def toSnake(str):
    string = re.sub('([A-Z])(\w+)([A-Z])', r'\1\2_\3', str)
    return string.lower()


a = input()
print(toSnake(a))
