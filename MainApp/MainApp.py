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

        app.DirectionF = int(direct)
        app.LineName = name.get()

    elif order == 2:

        app.DirectionS = int(direct)




def ChooseMenuF():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала
    window1 = Tk()
    window1.title("Первая точка")
    window1.geometry("250x250")
    window1.attributes('-topmost', True)
    # текстовая метка
    label1 = ttk.Label(window1, text="Наименование сигнала")
    label1.pack(anchor='n', padx=20, pady=10)

    EntryName = ttk.Entry(window1)
    EntryName.pack(anchor='n', padx=20, pady=5)

    position = {"padx":6, "pady":6, "anchor":"c"}
    WidthOfButton = 30

    directionUp = ttk.Button(window1, text='Направление ссылки на верх', width=WidthOfButton,
                             command=lambda: [GetLineParam(EntryName, 1, 90),
                                              Marker.getinfo1(1, app), ChooseMenuS(),
                                              window1.destroy()])
    directionUp.pack(**position)
    directionDown = ttk.Button(window1, text='Направление ссылки вниз', width=WidthOfButton,
                               command=lambda: [GetLineParam(EntryName, 1, -90),
                                                Marker.getinfo1(1, app), ChooseMenuS(),
                                                window1.destroy()])
    directionDown.pack(**position)
    directionRight = ttk.Button(window1, text='Направление ссылки вправо', width=WidthOfButton,
                                command=lambda: [GetLineParam(EntryName, 1, 0),
                                                 Marker.getinfo1(1, app), ChooseMenuS(),
                                                 window1.destroy()])
    directionRight.pack(**position)
    directionLeft = ttk.Button(window1, text='Направление ссылки влево', width=WidthOfButton,
                               command=lambda: [GetLineParam(EntryName, 1, 180),
                                                Marker.getinfo1(1, app),
                                                ChooseMenuS(),
                                                window1.destroy()])
    directionLeft.pack(**position)



def ChooseMenuS():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала
    window2 = Tk()
    window2.title("Вторая точка")
    window2.geometry("250x200")
    window2.attributes('-topmost', True)

    position = {"padx":6, "pady":6, "anchor":"c"}
    WidthOfButton = 30

    directionUp = ttk.Button(window2, text='Направление ссылки на верх', width=WidthOfButton,
                             command=lambda: [GetLineParam(None, 2, 90),
                                             Marker.getinfo1(2, app),
                                             Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                                                         app.Sy, app.LineName, app.DirectionS),
                                             window2.destroy()])
    directionUp.pack(**position)

    directionDown = ttk.Button(window2, text='Направление ссылки вниз', width=WidthOfButton,
                               command=lambda: [GetLineParam(None, 2, -90),
                                                Marker.getinfo1(2, app),
                                                Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                                                            app.Sy, app.LineName, app.DirectionS),
                                                window2.destroy()])
    directionDown.pack(**position)
    directionRight = ttk.Button(window2, text='Направление ссылки вправо', width=WidthOfButton,
                                command=lambda: [GetLineParam(None, 2, 0),
                                                 Marker.getinfo1(2, app),
                                                 Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                                                             app.Sy, app.LineName, app.DirectionS),
                                                 window2.destroy()])
    directionRight.pack(**position)
    directionLeft = ttk.Button(window2, text='Направление ссылки влево', width=WidthOfButton,
                               command=lambda: [GetLineParam(None, 2, 180),
                                                Marker.getinfo1(2, app),
                                                Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                                                            app.Sy, app.LineName, app.DirectionS),
                                                window2.destroy()])
    directionLeft.pack(**position)






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

# Добавить ссылку на текст в наименовании одного из сигналов



