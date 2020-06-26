import re
text = "\t\u001b[0;35mgoogle.com\u001b[0m \u001b[0;36m216.58.218.206\u001b[0m"
print("Original Text: ",text)
reaesc = re.compile(r'\x1b[^m]*m')
text2 = reaesc.sub('', text)
print("New Text: ",text2)
