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


def ChooseMenuF():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала
    def windAct(angle):
        GetLineParam(1, angle, EntryProfile, EntryName)
        Marker.getinfo1(1, app)
        ChooseMenuS()
        window1.destroy()

    # Настройка окна
    window1 = Toplevel(app.root)
    window1.title("Первая точка")
    window1.geometry("250x300")
    window1.attributes('-topmost', True)

    # текстовая метка
    label1 = ttk.Label(window1, text="Наименование сигнала", background='#f0f0f0')
    label1.pack(anchor='n', padx=20, pady=5)

    # Вывод в окно поля для получения наименования сигнала
    EntryName = ttk.Entry(window1)
    EntryName.pack(anchor='n', padx=20, pady=5)

    # текстовая метка
    label12 = ttk.Label(window1, text="Сечение провода в мм^2", background='#f0f0f0')
    label12.pack(anchor='n', padx=20, pady=5)

    # Вывод в окно поля для получения сечения проводника
    EntryProfile = ttk.Entry(window1)
    EntryProfile.pack(anchor='n', padx=20, pady=5)
    # текстовая метка
    label13 = ttk.Label(window1, text="Выберете направление ссылки", background='#f0f0f0')
    label13.pack(anchor='n', padx=20, pady=5)
    # Параметры кнопок

    WidthOfButton = 3

    # Вывод в окно функциональных кнопок
    # Направление ссылки вверх
    directionUp = Button(window1, text=chr(11205), font=('', 15), width=WidthOfButton,
                             command=lambda: windAct(UP))
    directionUp.pack(padx=6, pady=6, anchor='c')
    window1.bind('<Up>', lambda event: windAct(UP))
    app.root.bind('<Up>', lambda event: windAct(UP))
    # Направление ссылки вниз
    directionDown = Button(window1, text=chr(11206), font=('', 15), width=WidthOfButton,
                               command=lambda: windAct(DOWN))
    directionDown.place(relx=0.41,rely=0.8)
    window1.bind('<Down>', lambda event: windAct(DOWN))
    app.root.bind('<Down>', lambda event: windAct(DOWN))
    # Направление ссылки вправо
    directionRight = Button(window1, text=chr(11208), font=('', 15), width=WidthOfButton,
                                command=lambda: windAct(RIGHT))
    directionRight.place(relx=0.6,rely=0.66)
    window1.bind('<Right>', lambda event: windAct(RIGHT))
    app.root.bind('<Right>', lambda event: windAct(RIGHT))
    # Направление ссылки влево
    directionLeft = Button(window1, text=chr(11207), font=('', 15), width=WidthOfButton,
                               command=lambda: windAct(LEFT))
    directionLeft.place(relx=0.23,rely=0.66)
    window1.bind('<Left>', lambda event: windAct(LEFT))
    app.root.bind('<Left>', lambda event: windAct(LEFT))


def ChooseMenuS():
    # Получение получение информации о направлении ссылки
    # и наименование сигнала

    def windAct(angle):
        GetLineParam(2, angle ),
        Marker.getinfo1(2, app),
        Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                    app.Sy, app.LineName, app.DirectionS,
                    app.Profile),
        window2.destroy()

    # Настройка окна

    window2 = Toplevel(app.root)
    window2.title("Вторая точка")
    window2.geometry("280x200")
    window2.attributes('-topmost', True)
    #window2.focus_force()
    # Параметры кнопок

    WidthOfButton = 3
    label13 = ttk.Label(window2, text="Выберете направление второй ссылки", background='#f0f0f0')
    label13.pack(anchor='n', padx=20, pady=5)


    # Вывод в окно функциональных кнопок
    # Направление ссылки вверх

    directionUp = Button(window2, text=chr(11205), font=('', 15), width=WidthOfButton,
                             command=lambda: windAct(UP))
    directionUp.pack(padx=6, pady=6, anchor='c')
    window2.bind('<Up>', lambda event: windAct(UP))
    app.root.bind('<Up>', lambda event: windAct(UP))
    # Направление ссылки вниз
    directionDown = Button(window2, text=chr(11206), font=('', 15), width=WidthOfButton,
                               command=lambda: windAct(DOWN))
    directionDown.place(relx=0.41,rely=0.62)
    window2.bind('<Down>', lambda event: windAct(DOWN))
    app.root.bind('<Down>', lambda event: windAct(DOWN))
    # Направление ссылки вправо
    directionRight = Button(window2, text=chr(11208), font=('', 15), width=WidthOfButton,
                                command=lambda: windAct(RIGHT))
    directionRight.place(relx=0.6,rely=0.4)
    window2.bind('<Right>', lambda event: windAct(RIGHT))
    app.root.bind('<Right>', lambda event: windAct(RIGHT))
    # Направление ссылки влево
    directionLeft = Button(window2, text=chr(11207), font=('', 15), width=WidthOfButton,
                               command=lambda: windAct(LEFT))
    directionLeft.place(relx=0.23,rely=0.4)
    window2.bind('<Left>', lambda event: windAct(LEFT))
    app.root.bind('<Left>', lambda event: windAct(LEFT))






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
        btn = ttk.Button(self.root, text="Добавить ссылку", command=ChooseMenuF)
        btn.pack(expand=True)
        self.root.bind('<Return>', lambda event: ChooseMenuF())
    def run(self):
        self.root.mainloop()


app = App()
app.run()

# Сделать меню с настройками и справкой
# Добавить ввод направлений с клавиатуры




