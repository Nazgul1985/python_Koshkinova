import tkinter as tk


window = tk.Tk()
window.geometry("400x400")
# color 
current_color = "black"
brush_size = 5




# menu
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
        
menu = tk.Menu(window)
window.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Hello", command=hello)
file_menu.add_command(label="Пока", command=goodbye)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=quit_app)


#canvas
def change_color(new_color):
     current_color = new_color
     #canva.config(bg= current_color)
     #canva.configure(brushcolor=current_color)


def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    canva.create_oval(x1, y1, x2, y2, fill=current_color, outline=current_color)


canva = tk.Canvas(window, width=350, height=350)
canva.bind('<B1-Motion>', paint)
canva.pack()
# button
frame1 = tk.Frame(window)
frame1.pack()

button = tk.Button(frame1,
    text="Синий!",
    bg="blue",
    fg="black", 
    command=lambda: change_color('blue')
)

button2 = tk.Button(frame1,
    text="Зеленый!",
    bg="green",
    fg="black",
    command=lambda: change_color("green")
)
button3 = tk.Button(frame1,
    text="Красный!",
    bg="red",
    fg="black",
    command=lambda: change_color("red")
)

size_plus = tk.Button(window, text="+", width=3, command=increase_brush_size)
size_plus.pack(side="left")

size_minus = tk.Button(window, text="-", width=3, command=decrease_brush_size)
size_minus.pack(side="left")

button.pack(side='left')
button2.pack(side='left')
button3.pack(side='left')

window.mainloop()