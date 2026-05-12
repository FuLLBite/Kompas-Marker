from adodbapi.ado_consts import directions

import KFunc
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showerror

def getinfo1(order, app_obj):
    # Получение координат точки
    while True:

        x, y, result = KFunc.GetCursor()
        #print(f'{x}, {y}')
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
     # Поправочный коэффициент
    k = 5
    if Direction == 0: # Вправо
        CoordX = x + length + k
        CoordY = y
    elif Direction == 90: # Вверх
        CoordX = x - 5
        CoordY = y + length + k
    elif Direction == 180: # Влево
        CoordX = x - length - k
        CoordY = y
    elif Direction == -90: # Вниз
        CoordX = x - 5
        CoordY = y - length - k

    return CoordX, CoordY

def SignName(x, y, LineName, Direction):
    if Direction == 0: # Вправо
        KFunc.WriteText(x+4, y+2, LineName, hStr=3.5)
    elif Direction == 90: # Вверх
        KFunc.WriteText(x-2, y+4, LineName, 90, hStr=3.5)
    elif Direction == 180: # Влево
        KFunc.WriteText(x-4, y+2, LineName, hStr=3.5)
    elif Direction == -90: # Вниз
        KFunc.WriteText(x+2, y-4, LineName, 90, hStr=3.5)


def mark(Fx, Fy, DirectionF, Sx, Sy, LineName, DirectionS):

    length=15
    #print(f'Fx - {Fx}, тип {type(Fx)}')
    #print(f'Fy - {Fy}, тип {type(Fy)}')
    #print(f'DirectionF - {DirectionF}, тип {type(DirectionF)}')
    #print(f'Sx - {Sx}, тип {type(Sx)}')
    #print(f'Sy - {Sy}, тип {type(Sy)}')
    #print(f'LineName - {LineName}, тип {type(LineName)}')
    #print(f'DirectionS - {DirectionS}, тип {type(DirectionS)}')

    KFunc.MakeLine(Fx, Fy, DirectionF, length)
    KFunc.MakeLine(Sx, Sy, DirectionS, length)



    SignName(Fx, Fy, LineName, DirectionF)
    SignName(Sx, Sy, LineName, DirectionF)

    quantityTexts = KFunc.CountTexts()

    CoordXF, CoordYF = GetCoord(Fx, Fy, int(DirectionF), length)
    CoordXS, CoordYS = GetCoord(Sx, Sy, int(DirectionS), length)

    # Получение зон каждой точки
    FZona, FResultZona = KFunc.GetZona(CoordXF, CoordYF)
    SZona, SResultZona = KFunc.GetZona(CoordXS, CoordYS)

    # Обработка состояния ошибки при точке вне зоны и отсутствия зон в документе
    if FResultZona == 0 or SResultZona == 0:
        return '002'  # Точка вне документа или документ - не чертеж
    elif FResultZona == -1 or SResultZona == -1:
        return '003'  # В текущем документе нет разбиения на зоны

    # Вывод текстовой строки с обозначение зоны
    KFunc.WriteText(CoordXF, CoordYF, SZona)
    KFunc.WriteText(CoordXS, CoordYS, FZona)

    # Связывание локальными ссылками тектовые метки
    KFunc.HyperReference(quantityTexts, quantityTexts+1)
    KFunc.HyperReference(quantityTexts+1, quantityTexts)

    # Связывание тектовых меток гиперссылками
    KFunc.HyperLink(quantityTexts, quantityTexts+1)
    KFunc.HyperLink(quantityTexts+1, quantityTexts)