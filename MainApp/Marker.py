import KFunc

def mark():
    # Получение координат первой точки
    Fx, Fy, FResult = KFunc.GetCursor()
    # Получение координат второй точки
    Sx, Sy, SResult = KFunc.GetCursor()

    # Обработка состояния ошибки при неверных координатах
    if FResult != -1 or SResult != -1:
        return '001'  # код ошибки

    quantityTexts = KFunc.CountTexts()

    kp = 3 # коэффициент поправки расположения

    # Получение зон каждой точки
    FZona, FResultZona = KFunc.GetZona(Fx, Fy)
    SZona, SResultZona = KFunc.GetZona(Sx, Sy)

    # Обработка состояния ошибки при точке вне зоны и отсутствия зон в документе
    if FResultZona == 0 or SResultZona == 0:
        return '002'  # Точка вне документа или документ - не чертеж
    elif FResultZona == -1 or SResultZona == -1:
        return '003'  # В текущем документе нет разбиения на зоны

    # Вывод текстовой строки с обозначение зоны
    KFunc.WriteText(Fx - kp, Fy - kp, SZona)
    KFunc.WriteText(Sx - kp, Sy - kp, FZona)

    # Связывание локальными ссылками тектовые метки
    KFunc.HyperReference(quantityTexts, quantityTexts+1)
    KFunc.HyperReference(quantityTexts+1, quantityTexts)

    # Связывание тектовых меток гиперссылками
    KFunc.HyperLink(quantityTexts, quantityTexts+1)
    KFunc.HyperLink(quantityTexts+1, quantityTexts)