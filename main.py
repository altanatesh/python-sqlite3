import sqlite3 as sql
 
con = sql.connect("database.sqlite3", timeout=120)

cur = con.cursor()

cur.execute("CREATE TABLE table1(name TEXT, surname TEXT)")

name = input()
surname = input()

cur.execute("INSERT INTO table1 VALUES(?, ?)", (name, surname))
con.commit()

con.close()