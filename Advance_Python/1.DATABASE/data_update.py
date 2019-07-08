n = int(input("Enter number of entries : "))
import sqlite3 as sql 
db = sql.connect('student_data.db')
cursor = db.cursor()
cursor.execute('select id from student')
data = cursor.fetchall() # [ (1,),(2,),(3,) ]
initial_id = data[-1][0]
c = 1
for var in range(n) : 
    sid = initial_id + 1
    initial_id = sid
    name = input(f"Enter Name[{c}] : ").strip().lower()
    age = int(input(f"Enter Age[{c}] : "))
    address = input(f"Enter Address[{c}] : ").strip().lower()
    course = input(f"Enter Course[{c}] : ").strip().lower()
    print("\n\n")
    c = c + 1
    cmd = f"insert into student values ({sid},'{name}',{age},'{address}','{course}')"
    cursor.execute(cmd)
    db.commit()
    print("Person {name} is added to database \n\n")

