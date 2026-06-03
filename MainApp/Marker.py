import KFunc
from tkinter.messagebox import showerror

def getinfo(order, app_obj):
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
        CoordX = x + length + 1
        CoordY = y - 2
    elif Direction == 90: # Вверх
        CoordX = x + 2
        CoordY = y + length + 2
    elif Direction == 180: # Влево
        CoordX = x - length - 10
        CoordY = y - 2
    elif Direction == -90: # Вниз
        CoordX = x + 2
        CoordY = y - length - 7

    return CoordX, CoordY

def SignName(x, y, lineName, direction, profile):
    profile_mm = profile+' мм$2' if profile!='' else profile

    if direction == 0: # Вправо
        KFunc.WriteText(x+2, y+1, lineName, hStr=2.5)
        KFunc.WriteText(x+2, y-4.4, profile_mm, hStr=2.5)
    elif direction == 90: # Вверх
        KFunc.WriteText(x-1, y+2, lineName, 90, hStr=2.5)
        KFunc.WriteText(x+4.4, y+2, profile_mm, 90, hStr=2.5)
    elif direction == 180: # Влево
        KFunc.WriteText(x-len(lineName)*1.2-3, y+1, lineName, hStr=2.5)
        KFunc.WriteText(x-len(profile_mm)*1.2-3, y-4.4, profile_mm, hStr=2.5)
    elif direction == -90: # Вниз
        KFunc.WriteText(x-1, y-len(lineName)*1.2-3, lineName, 90, hStr=2.5)
        KFunc.WriteText(x+4.4, y-len(profile_mm)*1.2-3, profile_mm, 90, hStr=2.5)

def SignZone(coordX, coordY, zone, direction):

    if direction == 0 or direction == 90: # Вправо
        KFunc.WriteText(coordX, coordY, '(', angle=direction)
    elif direction == 180 or direction == -90: # Влево
        KFunc.WriteText(coordX, coordY, '(', angle=direction-180)


def MoveText(textObj, direction, coordX, coordY):
    if direction == -90:  # Вниз
        lenght = KFunc.LenghtText(coordX, coordY)
        #print(lenght)
        KFunc.MoveText(textObj, y=coordY - lenght + 6)
    elif direction == 180:  # Влево
        lenght = KFunc.LenghtText(coordX, coordY)
        #print(lenght)
        KFunc.MoveText(textObj, x=coordX - lenght + 9)




def mark(Fx, Fy, DirectionF, Sx, Sy, LineName, DirectionS, Profile):
    # Основная логика программы

    length = 15 # Длина линии ссылки

    # Отрисовка линии ссылки в поле чертежа
    KFunc.MakeLine(Fx, Fy, DirectionF, length)
    KFunc.MakeLine(Sx, Sy, DirectionS, length)

    # Вывод наименования сигнала в поле чертежа
    SignName(Fx, Fy, LineName, DirectionF, Profile)
    SignName(Sx, Sy, LineName, DirectionS, Profile)

    # Получение количества текстовых меток в документе
    IndexText = KFunc.CountTexts()

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
    SignZone(CoordXF, CoordYF, SZona, DirectionF)
    SignZone(CoordXS, CoordYS, FZona, DirectionS)

    # Связывание локальными ссылками тектовые метки
    KFunc.HyperReference(IndexText, IndexText+1, codeFun=-2)
    KFunc.HyperReference(IndexText+1, IndexText, codeFun=-2)

    KFunc.AddChar(IndexText, ', ', 2)
    KFunc.AddChar(IndexText+1, ', ', 2)

    KFunc.HyperReference(IndexText, IndexText + 1, codeFun=-1)
    KFunc.HyperReference(IndexText + 1, IndexText, codeFun=-1)

    KFunc.AddChar(IndexText, ')', 5)
    KFunc.AddChar(IndexText+1, ')', 5)

    MoveText(IndexText, DirectionF, CoordXF, CoordYF)
    MoveText(IndexText+1, DirectionS,CoordXS, CoordYS)

    # Связывание тектовых меток гиперссылками
    KFunc.HyperLink(IndexText, IndexText+1)
    KFunc.HyperLink(IndexText+1, IndexText)

    #print(IndexText)