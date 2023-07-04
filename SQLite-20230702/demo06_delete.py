import sqlite3 as db 

myDB = db.connect('0702.sqlite')

def deleteById(id):
  data = myDB.execute('select * from demo01 where did = %s'%(str(id)))
  myDB.commit()
  print(data.fetchall())
  if data.fetchall() is not None:
    myDB.execute('delete from demo01 where did = %s'%(str(id)))
    myDB.commit()
  else: print('Data Not Found')

deleteById(2)

myDB.close()