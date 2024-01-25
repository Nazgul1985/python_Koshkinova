import csv

data= [
    ['Title', 'Author', 'Year'],
    ['1984','Orwell', '1949'],
    ['The Little Prince','Exupery', '1944'],
    ['MasterMargarita','Bulgakov', '1940']
]
with open ('book.csv', 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open ('book.csv', 'r') as file:
    reader = csv.reader(file)
    row = list(reader) 

new_book = ['Book 4', 'Author 4', '2024']
row.append(new_book)

# Сохраняем в файл
with open('book.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row)

with open ('book.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print (row)
   
  