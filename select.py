import sqlite3

conn=sqlite3.connect('emobilis.db')
data=conn.execute("select * from Students")
for row in data:
    print("ID =",row[0])
    print("NAME =",row[1])
    print("AGE =",row[2])
    print("SCHOOl =",row[3], "\n")
conn.close()
