import re
import glob
import os
import xlrd

workbook = xlrd.open_workbook('/Users/talluri/Reg_test_tag.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
fdict = dict()
while curr_row < num_rows:
    curr_row += 1
    row = worksheet.row(curr_row)
    # print 'Row:', curr_row
    curr_cell = -1
    while curr_cell < num_cells:
        curr_cell += 1
        # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
        #cell_type = worksheet.cell_type(curr_row, curr_cell)
        cell_valu = worksheet.cell_value(curr_row, curr_cell)
        if curr_cell == 0:
            testname = cell_valu
        else:
            tag = cell_valu
    fdict[testname] = tag


os.chdir('/Users/talluri/asf/cloudstack/test/integration/component/')
files = glob.glob('test_*.py')
#for loop to iterate python unittest files
for filename in files:
    # print filename
    f = open(filename)
    g = open("/tmp/%s" % filename, 'w+')
    nameVsAttr = {}
    text = f.read()
    searchObj = re.findall(r'@attr\(tags\s*=\s*\[(.*)\]\)\n(.*)def.*(test_.*)\(self', text)
    if searchObj:
        for i in searchObj:
            nameVsAttr[i[2]] = i[0]
    # #TODO: make it generic to tag tests dynamically
    # text = f.read()
    modified_text = text
    for testname, attrib in nameVsAttr.items():
        q = re.compile(r'@attr\(tags\s*=\s*\[(.*)\]\)\n(.*)def (%s)\(self'%testname)
        searchObj = re.search(r'@attr\(tags\s*=\s*\[(.*)\]\)\n(.*)def.*(%s)\(self'%testname, modified_text)
        if searchObj:
            if testname in fdict.keys():
                tag = fdict[testname]
                tag = tag.replace(" ","")
                replacement = '@attr(tags=[%s, "%s"])\n%sdef %s(self' % (
                nameVsAttr[testname], tag, searchObj.group(2), testname)
                modified_text = q.sub(replacement, modified_text)
                print "%s>>%s:\"%s\" added tag"% (filename, testname, tag)
            else:
                print "  %s:%s doesn't have a new tag to be added"%(filename, testname)
        else:
            print "%s:%s there is no match for test"% (filename, testname)
    g.write(modified_text)
    f.close()
    g.close()

# for key, value in nameVsAttr.items():
#     print key,":",value


