import sqlite3 as db 

my_db = db.connect('0702.sqlite')

def insertRow(name, age):
    my_db.execute('insert into demo01 (name, age) values (?, ?)',(name, age))
    print(my_db)
    my_db.commit()
insertRow("Elaine", 28)

my_db.close()