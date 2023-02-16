import sqlite3
conn=sqlite3.connect('emobilis.db')
print("oppened db succesfully")
conn.execute(" CREATE TABLE Students "
             "(ID INT PRIMARY KEY NOT NULL,"
             "NAME TEXT NOT NULL,"
             "AGE INT NOT NULL,"
             "SCHOOL TEXT NOT NULL)")

print("Table created successfully")
conn.close()
