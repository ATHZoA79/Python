import sqlite3 as db 

my_db = db.connect('0702.sqlite')

def searchByColumn(col, text) :
    data = my_db.execute('select * from opendata_1 where %s = "%s"'%(col, text))
    for row in data:
        print(row)
    my_db.commit()

def query_search2():
    pass
searchByColumn("類別", "觀光類")

my_db.close() 