import Marker
from tkinter import *
from tkinter import ttk

def window1():
    window1 = Tk()
    window1.title("Первая точка")
    window1.geometry("250x300")
    window1.attributes('-topmost', True)
    directionUp = Button(window1, text="Закрыть",
                         command=window1.destroy)
    directionUp.pack(padx=6, pady=6, anchor='c')

class App:

    def __init__(self):
        # Настройка окна
        self.root = Tk()
        ttk.Style().theme_use('clam')
        self.root.title("Kompas Маркер")
        self.root.geometry("300x50")
        self.root.attributes('-topmost', True)


        # Добавление кнопки пользователя
        btn = ttk.Button(self.root, text="Добавить ссылку", command=window1)
        btn.pack(expand=True)
        self.root.bind('<Up>', lambda event: window1())
    def run(self):
        self.root.mainloop()
#command=ChooseMenuF)


app = App()
app.run()