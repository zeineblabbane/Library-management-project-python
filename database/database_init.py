import sqlite3

con = sqlite3.connect('sqlite.db')
cur = con.cursor()
cur.execute(
    "CREATE TABLE books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));")
cur.execute(
    "CREATE TABLE books_issued(bid varchar(20) primary key, issuedto varchar(30));")
con.commit()
print("Done")
con.close()