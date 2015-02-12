
import string
import xlwt
wbk = xlwt.Workbook()


sheet = wbk.add_sheet("TestCases")
# indexing is zero based, row then column
sheet.write(0,0,'test case')
sheet.write(0,1,'steps')
sheet.write(0,2,'Status')


row=1
tc = {"test1":"steps",
      "test2":"steps"}


f = open('/Users/talluri/testXl','r')
#
# f.write("%s, %s, %s\n"%('Test Case', 'Status', 'error'))
data = f.read()
list = data.split("prereq:\n")
count = 1
print list
for steps in list:
    testcase = "testVPC%d" %count
    col = 0
    while col <= 2:
        if col == 0:
            sheet.write(row, col, testcase)
        elif col == 1:
            sheet.write(row, col, "PreReq:\n:%s"%steps)
        else:
            sheet.write(row, col,"")
        col += 1
    # f.write("%s, %s, %s\n" % (case['name'],case['status'], errorStr))
    row += 1
    count +=1
f.close()

wbk.save('/Users/talluri/test_sanjeev.xls')
