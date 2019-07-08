import sqlite3 as sql 
db = sql.connect('student_data.db')
c = db.cursor() 
cmd = "select * from student"
c.execute(cmd) 
data = c.fetchall()

for each_row in data : 
    print(*each_row,sep='\t')

c.close()
db.close()
