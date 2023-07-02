import sqlite3 as db 
import json

my_db = db.connect('0702.sqlite')

def updateByColumn():
    datas = my_db.execute('update demo01 set name = "bred" where did = 1')
    print(datas)
    my_db.commit()

def updateById(name, id):
    datas = my_db.execute('select * from demo01 where did = %s'%(str(id)))
    # print(datas.fetchone())
    # pass
    my_db.commit()
    if datas.fetchone() is not None:
        datas = my_db.execute('update demo01 set name = ? where did = ?', (name, id))
        my_db.commit()
    else:
        print("id not found")

# updateByColumn()

updateById("David", 1)
my_db.close()