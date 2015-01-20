from jenkinsapi import jenkins

username = "" #add username
password = "" #add your password
URL = "http://ccp-tests.xenrt.xs.citrite.net/jenkins"
j = jenkins.Jenkins(URL, username, password)
jobclient = j.get_job('xenrt-regression-adv-hyperv')



p = jobclient.get_last_build().get_resultset()._data
cases = p["suites"][0]["cases"]
count = 0
f = open('./example.csv', 'w')
f.write("%s, %s, %s\n" % ('Test Case', 'Status', 'error'))
failed_tests = []
for case in cases:
    errorStr = case['errorDetails']
    #print "test case:{0}, status: {1}, error: {2}".format(case['name'], case['status'], errorStr)
    f.write("%s, %s, %s\n" % (case['name'],case['status'], errorStr))
    count += 1
f.close()
