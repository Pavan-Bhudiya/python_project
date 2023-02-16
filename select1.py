import sqlite3

conn=sqlite3.connect('Vehicle.db')
data=conn.execute("select * from Registration")
for row in data:
    print("ID =",row[0])
    print("Vehiclename =",row[1])
    print("Vehiclemake =",row[2])
    print("YEAR =",row[3], "\n")
conn.close()
