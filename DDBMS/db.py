import sqlite3 as sql

conn = sql.connect("testdb.db")
conn2 = sql.connect("common.db")
if conn:
    print("Successful conncetion 1!!")
else:
    print("Unsuccessful Connection 1")
conn.execute("CREATE TABLE IF NOT EXISTS test(id int)")
conn.execute("INSERT INTO test VALUES(55)")
conn.commit()

conn2.execute("CREATE TABLE IF NOT EXISTS co(id int, name varchar(25))")
conn2.execute("INSERT INTO co VALUES(1, 'abc')")
conn2.commit()

conn.close()
conn2.close()