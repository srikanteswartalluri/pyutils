__author__ = 'talluri'

class mail():
    def __repr__(self):
        return 'to:{1},\n mail <from:{0},\n  subject: {2}\n, body: {3}\n, num: {4}>'.format(self.from_id, self.to, self.subject,self.body,self.num)#new style format
    def __init__(self,from_id=None, to=None, subject=None, body=None, num=None):
        self.from_id = from_id
        self.to = to
        self.subject = subject
        self.body = body
        self.num = num
    def sendMail(self):
        pass
    def compose(self):
        pass
    def forward(self):
        pass
    def delMail(self):
        pass
    def archive(self):
        pass





class mailbox():
    def __repr__(self):
        return 'mailbox <{}>'.format(self.mails)
    def __init__(self,name=None , mails=None):
        self.name = name
        self.mails = []
    def addMail(self, mail):
        self.mails.append(mail)


m1 = mail()
mb = mailbox('inbox')

m1.from_id = 'someone@example.com'
m1.to = 'else@example.com'
m1.subject = 'hello subject'
m1.body = 'hello body'
m1.num = 4

mb.addMail(m1)

#print m1

m2 = mail()
m2.from_id = 'someone@example.com'
m2.to = 'else@example.com'
m2.subject = 'hello subject'
m2.body = 'hello body'
m2.num = 5
mb.addMail(m2)



#print mb.mails


m3 = mail('t@t.t','p@p.p','subj hello', 'body hello', '4')
mb.mails.append(m3)



print mb