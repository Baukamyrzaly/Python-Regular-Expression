import re
text = input("I \n' \nm \n \nB \na \nu \ny \nr \nz \nh \na \nn")
print(re.split('; |, |\*|\n',text))
