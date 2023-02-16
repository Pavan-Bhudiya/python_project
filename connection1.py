import sqlite3
conn=sqlite3.connect('Vehicle.db')
print("The database has opened succesfully")

conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (1,'Royals','Royce',2019)")
conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (2,'Range','Rover',2015)")
conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (3,'Porshe','Toyota',2016)")
conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (4,'Vitz','Audi',2018)")
conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (5,'Ferrai','Toyota',2019)")
conn.execute("INSERT INTO Registration(ID,Vehiclename,Vehiclemake,YEAR) VALUES (6,'Mercedez','BMW',2021)")

conn.commit()
print("records added successfully")
conn.close()