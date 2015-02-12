__author__ = 'talluri'
import re

email = 'talluri@gmail.com'

m = re.match('(\w+)@(\w+).(com)',email)

if m:
    print m.groups()

emails = 'talluri@gmail.com,support@gmail.com'

m = re.findall('(\w+)@(\w+).(com)',emails)

if m:
    for item in m:
        print item

string = 'People    say Python  is  cool'
print re.split('\s+',string)

print 'string is: {}'.format(' '.join(re.split('\s+',string)))
print string.split('\t')

l = ['Bangalore', 'Hyderabad', 'Mumbai']
print 'The places are : {}'.format(','.join(l))

print type(','.join(l))

print 'before sub',string
string = re.sub('\s+',' ',string)
print 'after substitute:', string

string = 'People    say Python  is  cool'
#sub only first match
string = re.sub('\s+',' ',string,count=2)
print string

