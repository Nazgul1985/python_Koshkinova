import sqlite3
conn = sqlite3.connect ('myDataBase.db')
cursor=conn.cursor()

try:
    conn.execute('BEGIN TRANSACTION')
    cursor.execute('UPDATE Products SET Price = 500 WHERE ProductID =1')
    cursor.execute('SAVEPOINT sp1')
    conn.execute('COMMIT')
except Exception as e:
    conn.execute ('ROLLBACK TO SAVE POINT sp1')
    print (f'Erorr:{e}')


sel_data_q = "SELECT * FROM Products;"
cursor.execute(sel_data_q)
rows= cursor.fetchall()
for row in rows:
    print(row)


conn.close()