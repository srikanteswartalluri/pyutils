__author__ = 'talluri'
import urllib
import re


num = "12345"
for i in xrange(1,400):
    page = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % num).read()
    pattern = "the next nothing is (\d+)"
    pattern2 = "Yes. Divide by two and keep going."
    re.compile(pattern)
    new_num = re.search(pattern, page)
    if new_num is not None:
        num = new_num.group(1)
    else:
        matched = re.match(r'Yes\. Divide by two and keep going\.', page)
        if matched is not None:
            num = int(num)
            num /= 2
    print "i:%s => num:%s" % (i, num)

