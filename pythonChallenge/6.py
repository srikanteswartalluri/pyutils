import zipfile
import re

zf = zipfile.ZipFile('/Users/talluri/Downloads/channel.zip', 'r')
start = 90052
bigString = ""


gd = dict((fl.filename, (zf.open(fl.filename).read(), fl.comment)) for fl in zf.filelist)

for filecount in xrange(len(gd.keys())):
    filename = "%s.txt" % start
    nextfile = re.search(r'Next nothing is (\d+)', gd[filename][0])
    if nextfile:
        #print "%s => %s" % (nextfile.group(1), p)
        start = nextfile.group(1)
        bigString += gd[filename][1]
    else:
        print filename, "=>", gd[filename]
        break


print bigString

