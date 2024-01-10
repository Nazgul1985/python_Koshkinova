import sqlite3
conn = sqlite3.connect ('myDataBase.db')
cursor=conn.cursor()
creat_table_q= '''
CREATE TABLE IF NOT EXISTS Orders(
ProductID INT PRIMARY KEY,
Name TEXT,
Price REAL
);''' 
cursor.execute(creat_table_q)
conn.commit()

insert_data_q2 = '''
INSERT INTO Orders (ProductID, Name, Price) VALUES
(3,'Lamp', 89.89),
(4, 'Printer', 45.56);
'''
cursor.execute(insert_data_q2)
conn.commit()

# Дааный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания
insert_data_q3 = '''
SELECT DISTINCT Category from Products 
'''
cursor.execute(insert_data_q3)
conn.commit()

# Дааный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания
insert_data_q3 = '''
SELECT Name, LastName from Emploes
WHERE balans>1000
'''
cursor.execute(insert_data_q3)
conn.commit()

# Дааный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания
insert_data_q3 = '''
SELECT * from Emploees
ORDER BY salary DESC
'''
cursor.execute(insert_data_q3)
conn.commit()

# Даnный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания

insert_data_q3 = '''
UPDATE Emploees
SET salary = salary*1,5
'''
cursor.execute(insert_data_q3)
conn.commit()

# Даnный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания

insert_data_q3 = '''
UPDATE Products 
SET price = price * 0,9
WHERE zapas <20
'''
cursor.execute(insert_data_q3)
conn.commit()


# Даnный запрос работать не будет, так как нет соответствующих полей в БД
# Просто прописано выполение домашнего задания

insert_data_q3 = '''
UPDATE Customers 
SET status = ''Active''
WHERE balans > 5000
'''
cursor.execute(insert_data_q3)
conn.commit()





sel_data_q = "SELECT * FROM Orders;"
cursor.execute(sel_data_q)
rows= cursor.fetchall()
for row in rows:
    print(row)