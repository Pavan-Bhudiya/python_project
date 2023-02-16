import sqlite3
conn=sqlite3.connect('Vehicle.db')
print("The database has opened succesfully")
conn.execute(" CREATE TABLE Registration "
             "(ID INT PRIMARY KEY NOT NULL,"
             "Vehiclename TEXT NOT NULL,"
             "Vehiclemake TEXT NOT NULL,"
             "YEAR  INT NOT NULL)")

print("Table created successfully")
conn.close()