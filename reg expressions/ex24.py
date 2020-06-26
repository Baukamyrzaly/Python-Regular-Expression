import re
def ab_match(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://static.hdrezka.ac/i/2014/2/5/z2104dc1f4444eo20x92n.jpg"
print(ab_match(url1))
