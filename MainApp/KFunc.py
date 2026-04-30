from Get_Kompas_API import get_kompas_api7

def GetCursor():
    # Функция возвращает координаты пространства 2D документа
    api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()
    ActiveDoc = obj5.ActiveDocument2D()
    request_info = obj5.GetParamStruct(constants.ko_RequestInfo)
    result, x, y = ActiveDoc.ksCursor(request_info, 0.0, 0.0, None)
    return x, y

def WriteText(x, y, text):
    # Функция выводит текстовую строку в пространстве 2D документа, по координатам
    # x - координаты по оси x
    # y - координаты по оси y
    # text - текстовая строка для вывода
    api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()
    ActiveDoc = obj5.ActiveDocument2D()
    ActiveDoc.ksText(x, y, 0, 5, 1, 0, text)

def GetZona(x, y):
    # Функция возвращает зону заданных координат на чертеже
    # x - координаты по оси x
    # y - координаты по оси y
    api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()
    ActiveDoc = obj5.ActiveDocument2D()
    Zona, result = ActiveDoc.ksGetZona(x, y)
    return Zona
