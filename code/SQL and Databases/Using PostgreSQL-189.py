## 3. Psycopg2 ##

import psycopg2 as p2
conn = p2.connect("dbname = dq user = dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("CREATE TABLE notes (id integer primary key, body text, title text)")
conn.close()

## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("CREATE TABLE notes (id integer primary key, body text, title text)")
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname = dq user = dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE TABLE facts(id integer PRIMARY KEY, country text, value integer)")

## 7. Executing queries ##

conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("INSERT INTO notes VALUES (1, 'Do more missions on Dataquest.', 'Dataquest reminder');")
cur.execute("SELECT * from notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("CREATE DATABASE income OWNER dq;")
conn.close()

## 9. Deleting a database ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit = True
cur = conn.cursor()
cur.execute("DROP DATABASE income;")
conn.close()