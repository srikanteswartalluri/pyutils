import re
#f = open("/Users/talluri/asf/cloudstack/test/integration/smoke/test_deploy_vms_with_varied_deploymentplanners.py")
f = open("test.file","w+")
f.write("hello\n")
f.write("test file\ntest kile\ntest kill\ntestgist")


f.seek(0,0)
count = 0
for line in f:
    #count =+ 1
    #if count==3:
    print "hello\n"
    print "line", line

# searchObj = re.search(r'.*test.*',text)
# if searchObj:
#    print "searchObj.group() : ", searchObj.group()
# else:
#    print "Nothing found!!"
# re.sub('test','Test',text)
# print "text:",text
# print "Name of the file: ", f.name
# print "Closed or not : ", f.closed
# print "Opening mode : ", f.mode
# print "Softspace flag : ", f.softspace
f.close()
