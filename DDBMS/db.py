import sqlite3 as sql

conn = sql.connect("testdb.db")
if conn:
    print("Successful conncetion!!")
else:
    print("Unsuccessful Connection")
conn.execute("CREATE TABLE IF NOT EXISTS test(id int)")
conn.commit()