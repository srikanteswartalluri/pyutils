__author__ = 'talluri'
def get_person_by_name(name):
    print 'Get person by name called'
def get_prerson_by_email(email):
    print 'Get person by email called'

field = 'name'
value = 'Talluri'

globals()['get_person_by_{}'.format(field)](value)

print globals()

field = 'email'
value = 'Talluri@cloud.com'

globals()['get_person_by_{}'.format(field)](value)