import tkinter as tk
from tkinter import Button

def details(title,x):
    def label(txt):
        tk.Label(text=txt,anchor="e",justify="left").pack()

    root = tk.Tk()
    root.title(title)
    root.geometry("400x480")
    label(x)
    button = Button(root,text="OK",command=root.destroy)
    button.pack()
    root.mainloop()