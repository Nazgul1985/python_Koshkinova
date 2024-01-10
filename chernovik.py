import sqlite3 
import csv
conn = sqlite3.connect ('myDataBase.db')
cursor=conn.cursor()

creat_table_q3= '''
CREATE TABLE IF NOT EXISTS Employees(
name TEXT,
phoneNumber TEXT,
email TEXT,
address TEXT,
userAgent TEXT,
hexcolor TEXT
);''' 

cursor.execute(creat_table_q3)
conn.commit()

with open ('example_1kb.csv','r') as cvsfile:
    csvreader = csv.reader(cvsfile)
    next (csvreader)
    cursor.execute ('INSERT INTO Employees VALUES(?,?,?,?,?,?);',csvreader)

conn.commit()
conn.close()





# sel_data_q = "SELECT * FROM Products;"
# cursor.execute(sel_data_q)
# rows= cursor.fetchall()
# for row in rows:
#     print(row)