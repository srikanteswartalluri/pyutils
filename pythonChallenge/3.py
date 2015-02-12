__author__ = 'talluri'
import re
import urllib

page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()

# text = "HELLOhHELLOhHELLOhHELhLLEhE"
pattern = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"
re.compile(pattern)
result = ''.join(re.findall(pattern, page))
print result
