import sqlite3
conn=sqlite3.connect('emobilis.db')
print("oppened db succesfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (1,'Erick',30,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (2,'Blissmal',21,'Pioneer')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (3,'Claris',17,'eMobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (4,'Bradley',18,'Brookhouse')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (5,'Moses',19,'Pioneer')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (6,'Faith',18,'Moi girls')")

conn.commit()
print("records added successfully")
conn.close()