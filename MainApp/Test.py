import Marker
from tkinter import *
from tkinter import ttk

# Константы
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

def GetLineParam(order, direct, profile=None ,name=None):
    # Получение параметров о наименовании и направлении ссылки сигнала
    # name - Наименование сигнала
    # order - Порядок
    # direct - Направление ссылки

    if order == 1:
        app.DirectionF = int(direct)
        app.LineName = name.get()
        app.Profile = profile.get()
    elif order == 2:
        app.DirectionS = int(direct)

class ChooseMenu:

    def windAct(self, angle):
        GetLineParam(1, angle, self.EntryProfile, self.EntryName)
        Marker.getinfo(1, app)
        #ChooseMenuS()
        self.window.destroy()

    def __init__(self, title):
        self.window = Toplevel(app.root)
        self.window.title(title)
        self.window.geometry("250x300")
        self.window.attributes('-topmost', True)

        # текстовая метка
        label1 = ttk.Label(self.window, text="Наименование сигнала", background='#f0f0f0')
        label1.pack(anchor='n', padx=20, pady=5)

        # Вывод в окно поля для получения наименования сигнала
        self.EntryName = ttk.Entry(self.window)
        self.EntryName.pack(anchor='n', padx=20, pady=5)

        # текстовая метка
        label12 = ttk.Label(self.window, text="Сечение провода в мм^2", background='#f0f0f0')
        label12.pack(anchor='n', padx=20, pady=5)

        # Вывод в окно поля для получения сечения проводника
        self.EntryProfile = ttk.Entry(self.window)
        self.EntryProfile.pack(anchor='n', padx=20, pady=5)
        # текстовая метка
        label13 = ttk.Label(self.window, text="Выберете направление ссылки", background='#f0f0f0')
        label13.pack(anchor='n', padx=20, pady=5)
        # Параметры кнопок

        WidthOfButton = 3

        # Вывод в окно функциональных кнопок
        # Направление ссылки вверх
        directionUp = Button(self.window, text=chr(11205), font=('', 15), width=WidthOfButton,
                             command=lambda: self.windAct(UP))
        directionUp.pack(padx=6, pady=6, anchor='c')
        self.window.bind('<Up>', lambda event: self.windAct(UP))
        app.root.bind('<Up>', lambda event: self.windAct(UP))
        # Направление ссылки вниз
        directionDown = Button(self.window, text=chr(11206), font=('', 15), width=WidthOfButton,
                               command=lambda: self.windAct(DOWN))
        directionDown.place(relx=0.41, rely=0.8)
        self.window.bind('<Down>', lambda event: self.windAct(DOWN))
        app.root.bind('<Down>', lambda event: self.windAct(DOWN))
        # Направление ссылки вправо
        directionRight = Button(self.window, text=chr(11208), font=('', 15), width=WidthOfButton,
                                command=lambda: self.windAct(RIGHT))
        directionRight.place(relx=0.6, rely=0.66)
        self.window.bind('<Right>', lambda event: self.windAct(RIGHT))
        app.root.bind('<Right>', lambda event: self.windAct(RIGHT))
        # Направление ссылки влево
        directionLeft = Button(self.window, text=chr(11207), font=('', 15), width=WidthOfButton,
                               command=lambda: self.windAct(LEFT))
        directionLeft.place(relx=0.23, rely=0.66)
        self.window.bind('<Left>', lambda event: self.windAct(LEFT))
        app.root.bind('<Left>', lambda event: self.windAct(LEFT))

class WindF(ChooseMenu):
    def __init__(self, parent):
        super().__init__(title="Первая точка")
        self.window.title()





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
        # Сечение проводника
        self.Profile = None
        # Направление первой ссылки
        self.DirectionF = None
        # Координаты второй точки
        self.Sx = None
        self.Sy = None
        # Направление второй ссылки
        self.DirectionS = None

        # Добавление кнопки пользователя
        btn = ttk.Button(self.root, text="Добавить ссылку", command=WindF)
        btn.pack(expand=True)
        self.root.bind('<Return>', lambda event: WindF())
    def run(self):
        self.root.mainloop()


app = App()
app.run()