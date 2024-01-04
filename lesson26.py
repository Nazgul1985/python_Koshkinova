import sqlite3
conn = sqlite3.connect ('myDataBase.db')
cursor=conn.cursor()

creat_table_q= '''
CREATE TABLE IF NOT EXISTS Products(
ProductID INT PRIMARY KEY,
Name TEXT,
Price REAL
);''' 
cursor.execute(creat_table_q)
conn.commit()

# insert_data_q = '''
# INSERT INTO Products (ProductID, Name, Price) VALUES
# (1,'Komp', 89),
# (2, 'Klava', 56);
# '''
# cursor.execute(insert_data_q)
# conn.commit()

insert_data_q2 = '''
INSERT INTO Products (ProductID, Name, Price) VALUES
(3,'Lamp', 89.89),
(4, 'Printer', 45.56);
'''
cursor.execute(insert_data_q2)
conn.commit()

sel_data_q = "SELECT * FROM Products;"
cursor.execute(sel_data_q)
rows= cursor.fetchall()
for row in rows:
    print(row)