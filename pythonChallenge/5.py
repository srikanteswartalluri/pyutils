__author__ = 'talluri'
import pickle
import urllib



page = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
obj = pickle.load(page)
for element in obj:
    #print element
    banner = ""
    for subelement in element:
        banner += subelement[0]*subelement[1]
    print banner
# b = open("t.txt",mode="w+")
# pickle.dump(obj, b)
# b.close()

