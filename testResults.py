from jenkinsapi import api, jenkins, job
import string
import xlwt
wbk = xlwt.Workbook()
username="talluri"
password='vmops.com'
j = jenkins.Jenkins('http://10.223.240.215',username,password)
#jobs = ['Adv_XS_BVT_Report', 'Adv_XS_Regression_Report', 'Basic_XS_BVT_Report', 'Basic_XS_Regression_Report']
    #, 'Eip_elb_BVT_Report', 'Eip_elb_XS_Regression_Report']
#jobs = ['Adv_XS_BVT_Report','Adv_VMware_BVT_Report', 'Adv_KVM_BVT_Report','Basic_KVM_BVT_Report', 'Basic_XS_BVT_Report']
#jobs = ['Adv_Simulator_BVT_Report']
#jobs = ['Adv_BVT_Report', 'Adv_Regression_Report']
jobs = [ 'Adv_Regression_Report']
for job in jobs:
    jobclient = j.get_job(job)

    sheet = wbk.add_sheet(job)
    # indexing is zero based, row then column
    sheet.write(0,0,'test case')
    sheet.write(0,1,'status')
    sheet.write(0,2,'Duration')
    sheet.write(0,3,'Error Description')
    sheet.write(0,4,'Comments')
    sheet.write(0,5,'Bug')
    sheet.write(0,6,'Bug_type')

    row=1




    #for matrix job
    #p = jobclient.get_last_build().get_resultset()._data
    ##cases = p["suites"][0]["cases"]
    ##print len(cases)
    #count = 0
    #f = open('/Users/talluri/example.csv','w')
    #f.write("%s, %s, %s\n"%('Test Case', 'Status', 'error'))
    #for childreport in p['childReports']:
    #    cases= childreport['result']['suites'][0]['cases']
    #    for case in cases:
    #        #if str(case['errorDetails']).find('Unable to stop') != -1:
    #        if case['status'] == 'FAILED' or case['status'] == 'ERROR' or case['status'] == 'REGRESSION':
    #            if count == 1:
    #                print case
    #            #print "test case:{0}, status: {1}, error: {2} ".format(case['name'], case['status'], case['errorDetails'])
    #            print "test case:{0}, status: {1}".format(case['name'], case['status'])
    #            f.write("%s, %s, %s\n" % (case['name'],case['status'], case['status']))
    #            count += 1
    #f.close()
    #print count

    p = jobclient.get_last_build().get_resultset()._data
    ##cases = p["suites"][0]["cases"]
    cases = p["suites"][0]["cases"]
    print len(cases)
    count = 0
    f = open('/Users/talluri/example.csv','w')
    g = open('/Users/talluri/error.txt','w')
    f.write("%s, %s, %s\n"%('Test Case', 'Status', 'error'))
    failed_tests = []
    for case in cases:
        if str(case['errorDetails']).find('Unable to stop') != -1:
        #if case['status'] == 'FAILED' or case['status'] == 'ERROR' or case['status'] == 'REGRESSION':
        #    if count == 1:
        #        print case
            #print "test case:{0}, status: {1}, error: {2} ".format(case['name'], case['status'], case['errorDetails'])\
            errorStr = 'Unable to stop'
            failed_tests.append(case['name'])
        elif str(case['errorDetails']).find('insuff') != -1:
            errorStr = 'insufficient capacity'
            failed_tests.append(case['name'])
        elif case['status'] == 'FAILED' or case['status'] == 'ERROR' or case['status'] == 'REGRESSION':
            errorStr = 'other'
        else:
            errorStr = case['errorDetails']
        print "test case:{0}, status: {1}, error: {2}".format(case['name'], case['status'], errorStr)
        col = 0
        while col <= 3:
            if col == 0:
                print "name"
                sheet.write(row, col, case['name'])
            elif col == 2:
                print "duration"
                sheet.write(row, col, case['duration'])
            elif col == 1:
                print "status"
                sheet.write(row, col,case['status'])
            else:
                print "error"
                lines = str(case['errorDetails']).split('\n')
                sheet.write(row, col,lines[0])

            col += 1
        f.write("%s, %s, %s\n" % (case['name'],case['status'], errorStr))
        g.write("########### Test name :{0}############\n".format(case['name']))
        g.write("########### STATUS :{0}############\n".format(case['status']))
        g.write("########### \n{0}\n################\n".format(case['errorDetails']))
        count += 1
        row += 1
    f.close()
    g.close()
#wbk.save('/Users/talluri/test_bvt.xls')
wbk.save('/Users/talluri/test_final.xls')
print count

print failed_tests