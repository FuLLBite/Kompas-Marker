from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")
    close_button = ttk.Button(window, text="Закрыть окно", command=lambda: window.destroy())
    close_button.pack(anchor="center", expand=1)

open_button = ttk.Button(text="Создать окно", command=click)
open_button.pack(anchor="center", expand=1)

root.mainloop()

