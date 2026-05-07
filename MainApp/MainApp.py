import Marker
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror

def TryToDo():

    CodeOfProcess = Marker.mark()
    if  CodeOfProcess == '001':
        showerror(title="Ошибка", message="Координаты заданы неверно")
    elif CodeOfProcess == '002':
        showerror(title="Ошибка", message="Точка вне документа или документ - не чертеж")
    elif CodeOfProcess == '003':
        showerror(title="Ошибка", message="В текущем документе нет разбиения на зоны")


# Настройка окна
root = Tk()
ttk.Style().theme_use('clam')
root.title("Kompas Маркер")
root.geometry("300x50")
root.attributes('-topmost', True)

# Добавление кнопки пользователя
btn = ttk.Button(text="Добавить ссылку", command=TryToDo)
btn.pack(expand=True)





root.mainloop()