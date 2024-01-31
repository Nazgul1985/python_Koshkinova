import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect ('project3.db')
cursor=conn.cursor()

creat_table_q= '''
CREATE TABLE IF NOT EXISTS Person(
PersonID INT PRIMARY KEY,
Name TEXT,
LastName TEXT
);''' 
cursor.execute(creat_table_q)
conn.commit()

# insert_data_q2 = '''
# INSERT INTO Orders (ProductID, Name, Price) VALUES
# (3,'Lamp', 89.89),
# (4, 'Printer', 45.56);
# '''
# cursor.execute(insert_data_q2)
# conn.commit()
root = tk.Tk()
root.geometry("400x400")

# def Add_info():
#     print ('Данные успешно внесены')

def add_user(id,name, last_name):
    cursor.execute('INSERT INTO Person (PersonID, Name, LastName) VALUES (?,?,?)', (id,name, last_name))
    conn.commit()

def open_new_window():
    new_window = tk.Tk()
    new_window.title("Новое окно")
    new_window.geometry("600x400")

    id_lbl = tk.Label(new_window, text="ИИН:")
    id_entry = tk.Entry(new_window)

    name_lbl = tk.Label(new_window, text="Имя:")
    name_entry = tk.Entry(new_window)

    last_n_lbl = tk.Label(new_window, text="Фамилия:")
    last_n_entry = tk.Entry(new_window)

    name_lbl.pack()
    name_entry.pack()
    last_n_lbl.pack()
    last_n_entry.pack()
    id_lbl.pack()
    id_entry.pack()
    en_btn = tk.Button(new_window, text="Добавить", command=add_user)
    en_btn.pack()

    id= id_entry.get()
    name = name_entry.get()
    last_name = last_n_entry.get()
    
    #add_user(id, name, last_name)
    new_window.mainloop()


def open_new_window1():
    new_window = tk.Tk()
    new_window.title("Новое окно")
    new_window.geometry("600x400")
    new_window.mainloop()

def check_login():
    username = login_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password":
        messagebox.showinfo("Успех", "Вход разрешен")
        open_new_window1()
    else:
        messagebox.showerror("Ошибка", "Неправильный логин или пароль")




# def login():
#     print("Выполняется вход...")
        
# def register():
#     print("Выполняется регистрация...")

root.title("Вход и регистрация")
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
login_label = tk.Label(frame1, text="Логин:")
login_entry = tk.Entry(frame1)

password_label = tk.Label(frame1, text="Пароль:")
password_entry = tk.Entry(frame1, show="*")
login_button = tk.Button(frame2, text="Вход", command=check_login)
register_button = tk.Button( frame2,text="Регистрация", command=open_new_window)
frame1.pack(padx=100, pady=50)
frame2.pack(ipadx=10, ipady=10)
login_label.pack()
login_entry.pack()
password_label.pack()
password_entry.pack()
login_button.pack()
register_button.pack()

login_button = tk.Button(frame2, text="Вход", command=check_login)
register_button = tk.Button( frame2,text="Регистрация", command=open_new_window)

root.mainloop()
