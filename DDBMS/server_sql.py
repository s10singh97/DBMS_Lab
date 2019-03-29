import pymysql as py

conn = py.Connect("172.21.4.120","ash","password","test")
if conn:
    print("Successfully Connected")

cursor = conn.cursor()
rows = cursor.execute("SHOW TABLES")
data = cursor.fetchall()
for row in data:
    print(row[0])
conn.close()