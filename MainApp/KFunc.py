from openpyxl.descriptors import Length
import math
from Get_Kompas_API import get_kompas_api7

api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()

def GetCursor():
    # Функция возвращает координаты пространства 2D документа

    ActiveDoc = obj5.ActiveDocument2D()
    request_info = obj5.GetParamStruct(constants.ko_RequestInfo)
    result, x, y = ActiveDoc.ksCursor(request_info, 0.0, 0.0, None)
    return x, y, result

def WriteText(x, y, text):
    # Функция выводит текстовую строку в пространстве 2D документа, по координатам
    # x - координаты по оси x
    # y - координаты по оси y
    # text - текстовая строка для вывода

    ActiveDoc = obj5.ActiveDocument2D()
    ActiveDoc.ksText(x, y, 0, 5, 1, 0, text)

def GetZona(x, y):
    # Функция возвращает зону заданных координат на чертеже
    # x - координаты по оси x
    # y - координаты по оси y

    ActiveDoc = obj5.ActiveDocument2D()
    Zona, result = ActiveDoc.ksGetZona(x, y)
    return Zona, result

def GetObject(x, y):
    # Функция возвращает объект в заданных координатах на чертеже
    # x - координаты по оси x
    # y - координаты по оси y

    ActiveDoc = obj5.ActiveDocument2D()
    Object = ActiveDoc.ksFindObj(x, y, 1)

    return Object

def HyperReference(IndEdited, IndObject):
    # Функция заменяет текст в текстовой метке IndEdited,
    # на ссылку расположения текстовой метки IndObject
    # IndEdited, IndObject - Индекс текстовой метки

    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iDrawingTexts = iDrawingContainer.DrawingTexts
    IndexCount = iDrawingTexts.Count
    iDrawingText0 = iDrawingTexts.DrawingText(IndObject) # Индекс текстовой метки
    iDrawingText1 = iDrawingTexts.DrawingText(IndEdited) # Индекс текстовой метки
    iText = KAPI7.IText(iDrawingText1)
    iTextLine = iText.TextLine(0) # Индекс строчки
    iTextItem = iTextLine.TextItem(0)
    iTextItem.ItemType = 0x2000
    iHypertextReferenceParam = KAPI7.IHypertextReferenceParam(iTextItem)
    iHypertextReferenceParam.LinkObject = iDrawingText0
    iHypertextReferenceParam.HypertextType = -1
    iTextItem.Update()
    iDrawingText1.Update()
    iDrawingText0.Update()


def CountTexts():
    # Функция возвращает количество текстовых меток

    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iDrawingTexts = iDrawingContainer.DrawingTexts
    IndexCount = iDrawingTexts.Count

    return IndexCount

def HyperLink(IndObject, IndEdited):
    # Функция связывает текстовые метки гиперссылками по индексам
    # IndEdited, IndObject - Индекс текстовой метки

    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iDrawingTexts = iDrawingContainer.DrawingTexts
    IndexCount = iDrawingTexts.Count
    iDrawingText0 = iDrawingTexts.DrawingText(IndObject) # Индекс текстовой метки
    iDrawingText1 = iDrawingTexts.DrawingText(IndEdited)

    kompas_document = api.ActiveDocument
    kompas_document_2d1 = KAPI7.IKompasDocument2D1(kompas_document)
    kompas_document_2d1.CreateHyperLink(iDrawingText1, 2, "", iDrawingText0, 0)

def MakeLine(x, y, length, angle):
    # Функция строит на активном виде отрезок
    # x - координаты по оси x
    # y - координаты по оси y
    # length - длина отрезка
    # angle - угол наклона отрезка

    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iLineSegments = iDrawingContainer.LineSegments
    iLineSegment = iLineSegments.Add()
    iLineSegment.X1 = x
    iLineSegment.Y1 = y
    iLineSegment.Length = length
    iLineSegment.Angle = angle
    iLineSegment.Update()

def TextPlace(x, y, angle):
    pass