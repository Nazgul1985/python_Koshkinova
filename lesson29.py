import sqlite3
conn = sqlite3.connect ('myDataBase1.db')
cursor=conn.cursor()

creat_table_Categor= '''
CREATE TABLE Categories (
  CategoryID INT PRIMARY KEY,
  CategoryName VARCHAR(50) NOT NULL
);''' 
cursor.execute(creat_table_Categor)


creat_table_Product= '''
  CREATE TABLE Product (
  ProductID INT,
  ProductName VARCHAR(50) NOT NULL,
  CategoryID INT,
  FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
);
'''
cursor.execute(creat_table_Product)


insert_data_Categ = '''
INSERT INTO Categories (CategoryID, CategoryName) 
VALUES (1, 'Electronics'),(2, 'Clothing'),(3, 'Home Goods');
'''
cursor.execute(insert_data_Categ)




insert_data_Prod = '''
INSERT INTO Product (ProductID, ProductName, CategoryID) 
VALUES (1, 'Smartphone', 1),(2, 'Laptop', 1),(3, 'T-Shirt', 2),(4, 'Jeans', 2),(5, 'Couch', 3),(6, 'Coffee Table', 3);
'''
cursor.execute(insert_data_Prod)

conn.commit()


sel_data_q = "SELECT * FROM Product;"
cursor.execute(sel_data_q)
rows= cursor.fetchall()
for row in rows:
    print(row)