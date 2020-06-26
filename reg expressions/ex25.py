import re
def dd_to_yyyy(a):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', a)
a1 = input()
print(dd_to_yyyy(a1))
