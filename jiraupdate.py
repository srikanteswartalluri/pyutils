from jenkinsapi import api, jenkins, job
username = ""
password = ""
j = jenkins.Jenkins('http://ccp-tests.xenrt.xs.citrite.net/jenkins',username, password)
jobclient = j.get_job('xenrt-regression-adv-hyperv')

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
f.write("%s, %s, %s\n"%('Test Case', 'Status', 'error'))
failed_tests = []
for case in cases:
    # if str(case['errorDetails']).find('Unable to stop') != -1:
    # #if case['status'] == 'FAILED' or case['status'] == 'ERROR' or case['status'] == 'REGRESSION':
    # #    if count == 1:
    # #        print case
    #     #print "test case:{0}, status: {1}, error: {2} ".format(case['name'], case['status'], case['errorDetails'])\
    #     errorStr = 'Unable to stop'
    #     failed_tests.append(case['name'])
    # elif str(case['errorDetails']).find('insuff') != -1:
    #     errorStr = 'insufficient capacity'
    #     failed_tests.append(case['name'])
    # elif case['status'] == 'FAILED' or case['status'] == 'ERROR' or case['status'] == 'REGRESSION':
    #     errorStr = 'other'
    # else:
    #     errorStr = case['errorDetails']
    errorStr = case['errorDetails']
    print "test case:{0}, status: {1}, error: {2}".format(case['name'], case['status'], errorStr)
    f.write("%s, %s, %s\n" % (case['name'],case['status'], errorStr))
    count += 1
f.close()
#print count

#print failed_tests


# # This script shows how to use the client in anonymous mode
# # against jira.atlassian.com.
#
# from jira.client import JIRA
#
# # By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# # (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# # Override this with the options parameter.
# options = {
#     'server': 'https://issues.apache.org/jira'
# }
# #jira = JIRA(options)
#
# jira = JIRA(options,basic_auth=('talluri', 'SiriEdu123'))
# # Get all projects viewable by anonymous users.
# projects = jira.projects()
#
# # Sort available project keys, then return the second, third, and fourth keys.
# keys = sorted([project.key for project in projects])[2:5]
#
# for method in  dir(jira):
#     print method
# # Get an issue.
# issue = jira.issue('CLOUDSTACK-5495')
# #print dir(issue)
#
# # Find all comments made by Atlassians on this issue.
# import re
# atl_comments = [comment for comment in issue.fields.comment.comments
#                 if re.search(r'talluri', comment.author.emailAddress)]
# #for cmnt in atl_comments:
# #    print cmnt.body
#
# # Add a comment to the issue.
# newcomment = "#comment added by script\nTotal tests failed in " \
#              "Regression Suite due to this issue: {0} \n List " \
#              "of tests: \n{1}".format(len(failed_tests), failed_tests)
# jira.add_comment(issue, newcomment)
#
# # Change the issue's summary and description.
# #issue.update(summary="I'm different!", description='Changed the summary to be different.')
#
# # You can update the entire labels field like this
# #issue.update(labels=['AAA', 'BBB'])
#
# # Or modify the List of existing labels. The new label is unicode with no spaces
# #issue.fields.labels.append(u'new_text')
# #issue.update(fields={"labels": issue.fields.labels})
#
# # Send the issue away for good.
# #issue.delete()
