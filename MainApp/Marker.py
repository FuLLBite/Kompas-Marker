import KFunc
from tkinter.messagebox import showerror

def getinfo1(order, app_obj):
    # Получение координат точки
    # order - Порядок
    # app_obj - объект
    while True:
        x, y, result = KFunc.GetCursor()
        if result != -1:
            showerror(title="Ошибка", message="Координаты заданы неверно")
        else:
            if order == 1:
                app_obj.Fx = x
                app_obj.Fy = y
            elif order == 2:
                app_obj.Sx = x
                app_obj.Sy = y
            break


def GetCoord(x, y, Direction, length):

    if Direction == 0: # Вправо
        CoordX = x + length
        CoordY = y - 2
    elif Direction == 90: # Вверх
        CoordX = x - 3
        CoordY = y + length + 3
    elif Direction == 180: # Влево
        CoordX = x - length - 10
        CoordY = y - 2
    elif Direction == -90: # Вниз
        CoordX = x - 5
        CoordY = y - length - 7

    return CoordX, CoordY

def SignName(x, y, lineName, direction, profile):
    profile_mm = profile+'мм$2' if profile!='' else profile
    if direction == 0: # Вправо
        KFunc.WriteText(x+2, y+2, lineName, hStr=3.5)
        KFunc.WriteText(x+2, y-6, profile_mm, hStr=3.5)
    elif direction == 90: # Вверх
        KFunc.WriteText(x-2, y+2, lineName, 90, hStr=3.5)
        KFunc.WriteText(x+6, y+2, profile_mm, 90, hStr=3.5)
    elif direction == 180: # Влево
        KFunc.WriteText(x-len(lineName)*2.2-3, y+2, lineName, hStr=3.5)
        KFunc.WriteText(x-len(profile_mm)*2.2, y-6, profile_mm, hStr=3.5)
    elif direction == -90: # Вниз
        KFunc.WriteText(x-2, y-len(lineName)*2.2-2, lineName, 90, hStr=3.5)
        KFunc.WriteText(x+8, y-len(profile_mm)*2.2, profile_mm, 90, hStr=3.5)



def mark(Fx, Fy, DirectionF, Sx, Sy, LineName, DirectionS, Profile):
    # Основная логика программы

    length = 20 # Длина линии ссылки

    # Отрисовка линии ссылки в поле чертежа
    KFunc.MakeLine(Fx, Fy, DirectionF, length)
    KFunc.MakeLine(Sx, Sy, DirectionS, length)

    # Вывод наименования сигнала в поле чертежа
    SignName(Fx, Fy, LineName, DirectionF, Profile)
    SignName(Sx, Sy, LineName, DirectionS, Profile)

    # Получение количества текстовых меток в документе
    quantityTexts = KFunc.CountTexts()

    # Задание координат для вывода ссылочных меток
    CoordXF, CoordYF = GetCoord(Fx, Fy, int(DirectionF), length)
    CoordXS, CoordYS = GetCoord(Sx, Sy, int(DirectionS), length)

    # Получение зон каждой точки
    FZona, FResultZona = KFunc.GetZona(CoordXF, CoordYF)
    SZona, SResultZona = KFunc.GetZona(CoordXS, CoordYS)

    # Обработка состояния ошибки при точке вне зоны и отсутствия зон в документе
    if FResultZona == 0 or SResultZona == 0:
        showerror(title="Ошибка", message="Точка вне документа или документ - не чертеж")
    elif FResultZona == -1 or SResultZona == -1:
        showerror(title="Ошибка", message="В текущем документе нет разбиения на зоны")

    # Вывод текстовой строки с обозначение зоны
    KFunc.WriteText(CoordXF, CoordYF, SZona)
    KFunc.WriteText(CoordXS, CoordYS, FZona)

    # Связывание локальными ссылками тектовые метки
    KFunc.HyperReference(quantityTexts, quantityTexts+1)
    KFunc.HyperReference(quantityTexts+1, quantityTexts)

    # Связывание тектовых меток гиперссылками
    KFunc.HyperLink(quantityTexts, quantityTexts+1)
    KFunc.HyperLink(quantityTexts+1, quantityTexts)
