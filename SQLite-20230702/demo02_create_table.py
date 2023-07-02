import sqlite3 as db 

my_db = db.connect('0702.sqlite')
create_query = "create table if not exists test02 (tid integer not null primary key autoincrement, name text not null)"

my_db.execute(create_query)
my_db.commit()

my_db.close()