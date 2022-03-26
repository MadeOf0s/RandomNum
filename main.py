from tkinter import *

win=Tk()

win.geometry("400x200")
win.title("RandomNums")

def write(str, font):
    l = Label(text = str)
    l.config(font =(font, 14))
    l.pack()

write("Hello", "Comic Sans MS")
button = Button(win, text = "Exit", command = win.destroy)
button.pack()

mainloop()