__author__ = 'talluri'
# find out title of the talk , views and comments

import re


f = open('talks.html','r')

content = f.read()
# print content


#matchObj = re.findall(r'<li class.*?<a title=(.*?)href.*?Views:.*?(\d+,?\d+).*?Comments:.*?(\d+).*?</li>', content, re.S|re.I|re.M)
matchObj = re.findall(r'<a title="(.*?)".*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*<p class="counts">Views: <strong class="notranslate">(\d,)+</strong>  \| Comments: <strong class="notranslate">(.*)', content, re.I|re.M)
if matchObj:
    for item in matchObj:
        print '{} \n title: {}, views: {}, comments: {}'.format("#"*80, item[0], item[1], item[2])

    # for match in  range(1,len(matchObj.group())-1):
        # print match
        # print "title:  ", matchObj.group(match)


# for lines in content:
#     #print lines
#     matchObj = re.search( r'Hendrik Poinar(.*)', lines, re.M|re.I)
#
#
#     if matchObj:
#         #print "matchObj.group() : ", matchObj.group()
#         print "title:  ", matchObj.group(1)
#     else:
#         pass#print "No match!!"
# # lines = f.readline()
#
# #  print lines
#     matchObj = re.match( r'.*\<a title=.*\"(.*)\" href.*\n', lines, re.M|re.I)
#     matchObj1 = re.match( r'.*Views:.*(\d+,).*Comments:.*(\d+).*\n', lines, re.M|re.I)
#
#     if matchObj:
#         # print "matchObj.group() : ", matchObj.group()
#         print "title:  ", matchObj.group(1)
#     else:
#         pass#print "No match!!"
#     if matchObj1:
#         # print "matchObj1.group() : ", matchObj1.group()
#         print "views : ", matchObj1.group(1)
#         print "comments:", matchObj1.group(2)
#     else:
#         pass#print "No match!!"
#


# print lines
#print type(f)
#print content
# f2 = open('test', 'w+')
# f2.write(content)
# print f2.read()
# f2.close()
f.close()
