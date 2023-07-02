import sqlite3 as db

my_db = db.connect('0702.sqlite')
print(my_db)

my_db.close()
print(my_db)