

# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.

from jira.client import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
options = {
    'server': 'https://issues.citrite.net'
}
#jira = JIRA(options)

jira = JIRA(options, basic_auth=('srikantest', 'SiriHyd23thChanging'))
# Get all projects viewable by anonymous users.
projects = jira.projects()

# Sort available project keys, then return the second, third, and fourth keys.
# keys = sorted([project.key for project in projects])[2:5]

# for method in  dir(jira):
#     print method

# for project in  projects:
#     print project
# Get an issue.

issues = jira.search_issues("project = CS AND affectedVersion = Goleta AND assignee in ('srikantest', 'sanjeevn')")
for issue in issues:
    # issue = jira.issue('CS-25512')
    # for cmt in issue.fields.comment.comments:
    #     print cmt.author.emailAddress
    # #print dir(issue)
    print #####################################
    print "status",issue.fields.status.name
    print "name",issue.fields.assignee.displayName
    print "email",issue.fields.assignee.emailAddress
    print "summary",issue.fields.summary
    if issue.fields.customfield_11335 is not None:
        print "timeEstimated", issue.fields.timetracking.originalEstimate
        print "remainingtime", issue.fields.timetracking.remainingEstimate
        print "sprintdetails",issue.fields.customfield_11335
    print #####################################

# # Find all comments made by Atlassians on this issue.
# import re
# atl_comments = [comment for comment in issue.fields.comment.comments
#                 if re.search(r'talluri', comment.author.emailAddress)]
# #for cmnt in atl_comments:
# #    print cmnt.body
#
# # Add a comment to the issue.
# newcomment = "#comment added by script\nTotal tests failed in " \
#              "Regression Suite due to this issue")
# jira.add_comment(issue, newcomment)

# Change the issue's summary and description.
#issue.update(summary="I'm different!", description='Changed the summary to be different.')

# You can update the entire labels field like this
#issue.update(labels=['AAA', 'BBB'])

# Or modify the List of existing labels. The new label is unicode with no spaces
#issue.fields.labels.append(u'new_text')
#issue.update(fields={"labels": issue.fields.labels})

# Send the issue away for good.
#issue.delete()
