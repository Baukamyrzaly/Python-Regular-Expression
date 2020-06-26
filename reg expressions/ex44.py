import re
text = "Astana city"
print(text)
redata = re.compile('Nursultan')
new_text = redata.sub('Nursultan', 'Astana city')
print (new_text)


