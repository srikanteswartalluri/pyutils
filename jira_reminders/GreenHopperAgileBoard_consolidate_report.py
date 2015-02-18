__author__ = 'talluri'
# This script shows how to use the client in anonymous mode
# against jira.atlassian.com.

# from six import print_ as print

from jira.client import GreenHopper
from jira.client import JIRA
from dateutil.parser import parse
from datetime import *
from subprocess import Popen, PIPE
import os
import errno
import sys



def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise


mail_id = {'shwetaag': 'Shweta.Agarwal@citrix.com',
           'manasav': 'manasa.veloori@citrix.com',
           'sanjeevn': 'sanjeev.neelarapu@citrix.com',
           'sureshsa': 'Suresh.Sadhu@citrix.com',
           'prashantkm': 'prashantkumar.mishra@citrix.com',
           'pavanb': 'Pavan.Bandarupally@citrix.com',
           't_gauravar': 'gaurav.aradhye@citrix.com',
           'srikantest': 'srikanteswararao.talluri@citrix.com',
           't_ashutosk': 'ashutosh.kelkar@citrix.com',
           'rpullela': 'raja.pullela@citrix.com',
           't_koteswarar': 'Koteswararao.Ravipati@citrix.com',
           't_deepthim2': 'deepthi.machiraju@citrix.com',
           'sarathkouk': 'sarath.kasi@citrix.com'
           }

mail_to_string = ""

for user in mail_id.keys():
    mail_to_string = mail_to_string + mail_id[user] + ","

def get_email_addr(jiraid):
    issue = jira.issue(id=jiraid)
    return issue.fields.assignee.emailAddress

def get_incompleted_per_person(issue, person):
    incompleted = []
    todo = []
    if issue.assignee == person:
        if issue.status.name.lower() == "In Progress".lower():
            incompleted = issue.key
        elif issue.status.name.lower() == "Open".lower():
            todo = issue.key
    return incompleted, todo

def get_completed_per_person(issue, person):
    completed = []
    if issue.assignee == person:
        if issue.status.name.lower() == "resolved".lower() or issue.status.name.lower() == "closed".lower():
            completed = issue.key
    return completed

def get_last_updated(jiraid):
    issue = jira.issue(id=jiraid)
    today = parse(date.today().strftime("%Y/%m/%d"))
    updated_date = parse(issue.fields.updated.split("T")[0])
    last_updated = today - updated_date
    if "," in str(last_updated):
        last_updated = str(last_updated).split(",")[0] + " ago"
    else:
        last_updated = "today"
    return last_updated

def print_report(fh, issue):
    fh.write("#####################################\n")
    fh.write("task: %s \n" % issue.key)
    fh.write("status: %s\n" % issue.status.name)
    fh.write("username: %s\n" % issue.assignee)
    fh.write("Name: %s\n" % issue.assigneeName)
    fh.write("Email: %s\n" % mail_id[issue.assignee])
    fh.write("summary: %s\n" % issue.summary)
    if hasattr(issue, 'issue.estimateStatistic.statFieldValue.value'):
        fh.write("timeEstimated: %s\n" % issue.estimateStatistic.statFieldValue.value)
    if hasattr(issue, 'issue.trackingStatistic.statFieldValue.text'):
        fh.write("remainingtime: %s\n", issue.trackingStatistic.statFieldValue.text)
    fh.write("\n#####################################\n")
    #print issue.assignee, ":", get_email_addr(issue.key), ","


# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
# GreenHopper is a plugin in a JIRA instance
options = {
    'server': 'https://issues.citrite.net'
}

jira = JIRA(options)
gh = JIRA(options)

# Get all boards viewable by anonymous users.
# boards = gh.boards()
board_id = ""
board_name = ""
sprint_id = ""
# for board in boards:
#     if 'scrum-hyd' in board.name.lower():
#         board_id = board.id
#         board_name = board.name
#         break
# Get the sprints in a specific board
if len(sys.argv) < 3:
    print "Requires board_id and sprint_id as inputs"
    sys.exit(2)
board_id = sys.argv[1]
sprint_id = sys.argv[2]
board_name = 'CCP QA Scrum  - Hyd'

print("GreenHopper board: %s (%s)" % (board_name, board_id))
#sprints = gh.sprints(board_id)
sprint = gh.sprint_info(board_id, sprint_id)

# List the incomplete issues in each sprint
#for sprint in sprints:
sprint_id = sprint['id']
print("Sprint: %s" % sprint['name'])
incompleted_issues = gh.incompleted_issues(board_id, sprint_id)
completed_issues = gh.completed_issues(board_id, sprint_id)
#print("Incomplete issues: %s" % ', '.join(issue.key for issue in incompleted_issues))
report = {}

for person in mail_id.keys():
    count = 0
    report[person] = {"Completed": [],
                      "Incompleted": [],
                      "Todo": []
    }
    for issue in incompleted_issues:
        if issue.assignee == person:
            count = count + 1
            incompleted, todo = get_incompleted_per_person(issue, person)
            if incompleted:
                last_updated = get_last_updated(incompleted)
                report[person]["Incompleted"].append({"id": incompleted,
                                                      "last_updated": last_updated})
            if todo:
                report[person]["Todo"].append(todo)
    for issue in completed_issues:
        if issue.assignee == person:
            count = count + 1
            completed = get_completed_per_person(issue, person)
            if completed:
                report[person]["Completed"].append(completed)

EmptyPeople = []
for entry in report.keys():
    if len(report[entry]["Incompleted"]) == 0:
        EmptyPeople.append(entry)


file = open('dump.txt', 'w')
if len(EmptyPeople) != 0:
    file.write("\nPeople with 0 tasks 'In Progress': %s\n" % EmptyPeople)
    file.write("Please move your tasks to 'In Progress'\n")

for entry in report.keys():
    # print "%s: Completed: %s Incompleted: %s, Todo: %s\n" % (entry, len(report[entry]["Completed"]),
    #                                                          len(report[entry]["Incompleted"]),
    #                                                          len(report[entry]["Todo"])
    # )
    file.write("\n\n%s:\n\tCompleted: %s\n" % (entry, report[entry]["Completed"]))
    file.write("\tIn Progress:[\n")
    for in_prog in report[entry]["Incompleted"]:
        file.write("\t\t{%s, last updated: %s}, \n" % (in_prog["id"],
                                                       in_prog["last_updated"])
        )
    file.write("\t]\n")
    file.write("\tTodo: %s\n" % report[entry]["Todo"])


file.close()


output = Popen(['mail -s "Greenfield Sprint- consolidated daily report" %s < %s' % (mail_to_string,
                                                                                "dump.txt")],
                       stdout=PIPE,
                       stderr=PIPE,
                       shell=True)
(out, err) = output.communicate()



