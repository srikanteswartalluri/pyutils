__author__ = 'talluri'
place_to_state_map = {'Bangalore' : 'Karnataka',
                      'Hyderabad' : 'AndhraPradesh',
                      'Vijayawada': 'AndhraPradesh'
}
print place_to_state_map['Bangalore']
print place_to_state_map['Vijayawada']
if 'Vijayawada' in place_to_state_map:
    print True
else:
    print False

mail = {
    'from' : 'talluri@talluri.com',
    'to':'talluri@talluri.com',
    'subject':'hello',
    'body':'hello body'
}
mail2 = {
    'from' : 'talluri1@talluri.com',
    'to':'talluri1@talluri.com',
    'subject':'hello1',
    'body':'hello1 body'
}
mail_boxes = {'inbox':[]}
mail_boxes['inbox'].append(mail)
mail_boxes['inbox'].append(mail2)
# print mail_boxes

mail_boxes['special'] = {}

mail_boxes['special']['specialkey'] = "specialvalue"

# print mail_boxes['special']

for i in mail_boxes.keys():
    print i,":",mail_boxes[i]

for mails in mail_boxes['inbox']:
    if mails['from'] == 'talluri1@talluri.com':
        mails['subject'] = 'talluri hello'

for i in mail_boxes.keys():
    print i,":",mail_boxes[i]

x =  mail_boxes.items()
print 'a'*80,x[0]

