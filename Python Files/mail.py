import db
import db1
import connect
import connect1

m = input()
statename = input()



db.state(statename)
db1.state(statename)
connect.country(m,statename)
connect1.country(m,statename)