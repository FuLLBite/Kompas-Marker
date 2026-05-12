import KFunc
import Marker
import tkinter
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


def GetLineParam(name, order, direct):

    if order == 1:
        #print(f'direct1 - {direct}, type - {type(direct)}')
        app.DirectionF = int(direct)
        app.LineName = name.get()

    elif order == 2:
        #print(f'direct1 - {direct}, type - {type(direct)}')
        app.DirectionS = int(direct)




def ChooseMenuF():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала
    window1 = Tk()
    window1.title("Первая точка")
    window1.geometry("250x300")
    window1.attributes('-topmost', True)
    # текстовая метка
    label1 = ttk.Label(window1, text="Наименование сигнала")
    label1.pack(anchor='n', padx=20, pady=10)

    EntryName = ttk.Entry(window1)
    EntryName.pack(anchor='n', padx=20, pady=5)

    position = {"padx":6, "pady":6, "anchor":"w"}



    DirectionF = IntVar()

    directionUp = ttk.Radiobutton(window1, text='Направление ссылки на верх', value=90, variable=DirectionF, command=lambda: GetLineParam(EntryName, 1, 90))
    directionUp.pack(**position)
    directionDown = ttk.Radiobutton(window1, text='Направление ссылки вниз', value=-90, variable=DirectionF, command=lambda: GetLineParam(EntryName, 1, -90))
    directionDown.pack(**position)
    directionUp = ttk.Radiobutton(window1, text='Направление ссылки вправо', value=0, variable=DirectionF, command=lambda: GetLineParam(EntryName, 1, 0))
    directionUp.pack(**position)
    directionDown = ttk.Radiobutton(window1, text='Направление ссылки влево', value=180, variable=DirectionF, command=lambda: GetLineParam(EntryName, 1, 180))
    directionDown.pack(**position)

    buttonNext = ttk.Button(window1, text="Следующая точка", command=lambda: [ChooseMenuS(), window1.destroy()])
    buttonNext.place(relx=.95, rely=.9, anchor="se")

    buttonGetInfo = ttk.Button(window1, text="Указать точку", command=lambda: Marker.getinfo1(1, app))
    buttonGetInfo .place(relx=.05, rely=.9, anchor="sw")



def ChooseMenuS():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала
    window2 = Tk()
    window2.title("Вторая точка")
    window2.geometry("250x250")
    window2.attributes('-topmost', True)

    position = {"padx":6, "pady":6, "anchor":"w"}

    DirectionS = IntVar()

    directionUp = ttk.Radiobutton(window2, text='Направление ссылки на верх', value=90, variable=app.DirectionS, command=lambda: GetLineParam(None, 2, 90))
    directionUp.pack(**position)
    directionDown = ttk.Radiobutton(window2, text='Направление ссылки вниз', value=-90, variable=app.DirectionS, command=lambda: GetLineParam(None, 2, -90))
    directionDown.pack(**position)
    directionUp = ttk.Radiobutton(window2, text='Направление ссылки вправо', value=0, variable=app.DirectionS, command=lambda: GetLineParam(None, 2, 0))
    directionUp.pack(**position)
    directionDown = ttk.Radiobutton(window2, text='Направление ссылки влево', value=180, variable=app.DirectionS, command=lambda: GetLineParam(None, 2, 180))
    directionDown.pack(**position)

    buttonGetInfo = ttk.Button(window2, text="Указать точку", command=lambda: [Marker.getinfo1(2, app)])
    buttonGetInfo .place(relx=.05, rely=.9, anchor="sw")

    buttonFinish = ttk.Button(window2, text="Завершить", command=lambda: [Marker.mark(app.Fx,
                                                                                      app.Fy,
                                                                                      app.DirectionF,
                                                                                      app.Sx,
                                                                                      app.Sy,
                                                                                      app.LineName,
                                                                                      app.DirectionS),
                                                                          window2.destroy()])
    buttonFinish.place(relx=.95, rely=.9, anchor="se")





class App:
    def __init__(self):
        # Настройка окна
        self.root = Tk()
        ttk.Style().theme_use('clam')
        self.root.title("Kompas Маркер")
        self.root.geometry("300x50")
        self.root.attributes('-topmost', True)
        # Координаты первой точки
        self.Fx = None
        self.Fy = None
        # Наименование линии
        self.LineName = None
        # Направление первой ссылки
        self.DirectionF = None
        # Координаты второй точки
        self.Sx = None
        self.Sy = None
        # Направление второй ссылки
        self.DirectionS = None

        # Добавление кнопки пользователя
        btn = ttk.Button(self.root, text="Добавить ссылку", command=ChooseMenuF)
        btn.pack(expand=True)
    def run(self):
        self.root.mainloop()


app = App()
app.run()


# Исправить ошибку - не верные ссылки (Баг при частом запуске)

# Исправить расположение текста наименования сигнала

# Сделать указание точки по Radiobutton, убрать лишние кнопки

# Добавить адаптивность к длине наименования сигнала

# Добавить ссылку на текст в наименовании одного из сигналов



