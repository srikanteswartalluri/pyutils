__author__ = 'talluri'

#establish socket(ip,port,protocol) connection
#cursor

import sqlite3

conn = sqlite3.connect('people.db') #in this case a file interaction


print conn

# print help(conn)

c = conn.cursor()

c.execute("CREATE TABLE mail(from_id text,to_id text, subject text, body text)")

c.execute("INSERT INTO mail VALUES('t@t.com', 'p@p.p', 'hello', 'hello body')")

c.execute("INSERT INTO mail VALUES('t@1t.com', 'p1@p.p', 'hello1', 'hello body1')")

conn.commit()

c.execute("SELECT * FROM mail")

r = c.fetchall()

for item in r:
    print item
