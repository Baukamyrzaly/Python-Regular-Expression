import re


def toCamel(str):
    return ''.join(x.capitalize() for x in str)


a = input().split('_')
print(toCamel(a))
