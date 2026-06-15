from tkinter import *

root = Tk()
root.title("Drag and Drop Demo")
root.geometry("400x300")

label = Label(root, text="Drag Me", bg="lightblue")
label.place(x=100, y=100)

def start_drag(event):
    label.startX = event.x
    label.startY = event.y

def drag(event):
    x = label.winfo_x() - label.startX + event.x
    y = label.winfo_y() - label.startY + event.y
    label.place(x=x, y=y)

label.bind("<Button-1>", start_drag)
label.bind("<B1-Motion>", drag)

root.mainloop()
