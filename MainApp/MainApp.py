import Marker, KompasMacProperty
from tkinter import *
from tkinter import ttk


# Константы
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class ChooseMenu:

    def windAct(self, angle, order):

        Marker.getinfo(order, app)
        if order == 1:
            app.DirectionF = int(angle)
            app.LineName = self.EntryName.get()
            app.Profile = self.EntryProfile.get()
            ChooseMenuS = ChooseMenu("Вторая точка", False)
            self.window.destroy()
        elif order == 2:
            app.DirectionS = int(angle)
            Marker.mark(app.Fx, app.Fy, app.DirectionF, app.Sx,
                        app.Sy, app.LineName, app.DirectionS,
                        app.Profile)
            self.window.destroy()


    def TextParam(self):
        # Текстовые метки и поля для ввода данных
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


    def __init__(self, title, FMenu):
        self.window = Toplevel(app.root)
        self.window.title(title)
        self.window.attributes('-topmost', True)

        order = 1 # Порядок выбора меню
        RLy = 0.66 # Координата по Y кнопок выбора направления ссылок лево/право
        Dy = 0.8 # Координата по Y кнопок выбора направления ссылок вниз

        if FMenu:
            self.window.geometry("250x300")
            self.TextParam()
        else:
            order = 2
            RLy = 0.35
            Dy = 0.65
            self.window.geometry("250x150")

        # Параметры кнопок

        WidthOfButton = 3

        # Вывод в окно функциональных кнопок
        # Направление ссылки вверх
        directionUp = Button(self.window, text=chr(11205), font=('', 15), width=WidthOfButton,
                             command=lambda: self.windAct(UP, order))
        directionUp.pack(padx=6, pady=6, anchor='c')

        self.window.bind('<Up>', lambda event: self.windAct(UP, order))
        app.root.bind('<Up>', lambda event: self.windAct(UP, order))
        # Направление ссылки вниз
        directionDown = Button(self.window, text=chr(11206), font=('', 15), width=WidthOfButton,
                               command=lambda: self.windAct(DOWN, order))
        directionDown.place(relx=0.41, rely=Dy)
        self.window.bind('<Down>', lambda event: self.windAct(DOWN, order))
        app.root.bind('<Down>', lambda event: self.windAct(DOWN, order))
        # Направление ссылки вправо
        directionRight = Button(self.window, text=chr(11208), font=('', 15), width=WidthOfButton,
                                command=lambda: self.windAct(RIGHT, order))
        directionRight.place(relx=0.6, rely=RLy)
        self.window.bind('<Right>', lambda event: self.windAct(RIGHT, order))
        app.root.bind('<Right>', lambda event: self.windAct(RIGHT, order))
        # Направление ссылки влево
        directionLeft = Button(self.window, text=chr(11207), font=('', 15), width=WidthOfButton,
                               command=lambda: self.windAct(LEFT, order))
        directionLeft.place(relx=0.23, rely=RLy)
        self.window.bind('<Left>', lambda event: self.windAct(LEFT, order))
        app.root.bind('<Left>', lambda event: self.windAct(LEFT, order))




class App:
    def __init__(self):
        # Настройка окна
        self.root = Tk()
        ttk.Style().theme_use('clam')
        self.root.title("Kompas Маркер")
        self.root.geometry("300x100")
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
        btn = ttk.Button(self.root, text="Добавить ссылку", command = lambda: ChooseMenu("Первая точка", True))
        btn.pack(expand=True)
        self.root.bind('<Return>', lambda event: ChooseMenu("Первая точка"))

        # Добавление кнопки пользователя для преобразования макроэлементов
        mc_btn = ttk.Button(self.root, text="Преобразовать макроэлементы", command = lambda: KompasMacProperty.SetMacroProp())
        mc_btn.pack(expand=True)

    def run(self):
        self.root.mainloop()


app = App()
app.run()

# Сделать возсожность настраивать шрифты

# Сделать автоматический перечень




