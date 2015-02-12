import re
f = open("/Users/talluri/asf/cloudstack/test/integration/smoke/test_vpc_vpn.py")
#f = open("test.file",'r+')
#f.seek(10,0)
#text = f.read()
fdict = {}
count = 0
for line in f:
    count = count + 1
    #if count==3:
    #print "line", line
    #searchObj = re.search(r'attr\(tags=(.*)\n.*def (test.*)\(self\):',line)
    searchObj = re.search(r'@attr\(tags=',line)
    if searchObj:
       print "searchObj.group() : ", searchObj.group()
       fdict[count] = line
       # print "count", count
       # print "line", line

    searchObj = re.search(r'def test_',line)
    if searchObj:
       print "searchObj.group() : ", searchObj.group()
       fdict[count] = line
       # print "count", count
       # print "line", line

for key, value  in fdict.items():
    print key,value
       #re.sub(searchObj.group(1),
       #print "searchObj.group(1) : ", searchObj.group(1)
       #print "searchObj.group(2) : ", searchObj.group(2)
    # else:
    #    print ""
#re.sub(r'attr\(tags=(.*)\n.*def (test.*)\(self\):',r'attr\(tags=(.*)\n.*def (test.*)\(self\):'
#print "text:",text
# print "Name of the file: ", f.name
# print "Closed or not : ", f.closed
# print "Opening mode : ", f.mode
# print "Softspace flag : ", f.softspace
f.close()
