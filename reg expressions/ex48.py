def d_number(num):
    import re
    decimal = re.compile(r"""^[0-9]+(\.[0-9]{1,2})$""")
    result = decimal.search(num)
    return bool(result)
d=input()
print(d_number(d))
