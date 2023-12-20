import tkinter as tk

#Добавил глобальное значение current_color теперь при нажатие на цвет кисть меняет свой цвет

window = tk.Tk()
window.geometry("400x400")

current_color = "black"
brush_size = 5

def hello():
    print("Hello!")

def goodbye():
    print("Goodbye!")

def quit_app():
    window.destroy()

def increase_brush_size():
    global brush_size
    brush_size += 5

def decrease_brush_size():
    global brush_size
    if brush_size > 1:
        brush_size -= 1

def change_color(new_color):
    global current_color
    current_color = new_color

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canva.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=brush_size)

canva = tk.Canvas(window, width=350, height=350)
canva.bind('<B1-Motion>', paint)
canva.pack()

frame1 = tk.Frame(window)
frame1.pack()

button = tk.Button(frame1, text="Синий!", bg="blue", fg="black", command=lambda: change_color('blue'))
button2 = tk.Button(frame1, text="Зеленый!", bg="green", fg="black", command=lambda: change_color("green"))
button3 = tk.Button(frame1, text="Красный!", bg="red", fg="black", command=lambda: change_color("red"))

size_plus = tk.Button(window, text="+", width=3, command=increase_brush_size)
size_plus.pack(side="left")

size_minus = tk.Button(window, text="-", width=3, command=decrease_brush_size)
size_minus.pack(side="left")

button.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

window.mainloop()
import tkinter as tk

window = tk.Tk()
window.geometry("400x400")

current_color = "black"
brush_size = 5

def hello():
    print("Hello!")

def goodbye():
    print("Goodbye!")

def quit_app():
    window.destroy()

def increase_brush_size():
    global brush_size
    brush_size += 5

def decrease_brush_size():
    global brush_size
    if brush_size > 1:
        brush_size -= 1

def change_color(new_color):
    global current_color
    current_color = new_color

def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canva.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color, width=brush_size)

canva = tk.Canvas(window, width=350, height=350)
canva.bind('<B1-Motion>', paint)
canva.pack()

frame1 = tk.Frame(window)
frame1.pack()

button = tk.Button(frame1, text="Синий!", bg="blue", fg="black", command=lambda: change_color('blue'))
button2 = tk.Button(frame1, text="Зеленый!", bg="green", fg="black", command=lambda: change_color("green"))
button3 = tk.Button(frame1, text="Красный!", bg="red", fg="black", command=lambda: change_color("red"))

size_plus = tk.Button(window, text="+", width=3, command=increase_brush_size)
size_plus.pack(side="left")

size_minus = tk.Button(window, text="-", width=3, command=decrease_brush_size)
size_minus.pack(side="left")

button.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

window.mainloop()
