import re
def space_at_the_beginning_capital(str):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str)
a=input()
print(space_at_the_beginning_capital(a))
