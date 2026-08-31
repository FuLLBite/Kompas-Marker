from Get_Kompas_API import get_kompas_api7
from win32com.client import CastTo
import pythoncom
from pythoncom import VT_EMPTY
from win32com.client import Dispatch, gencache, VARIANT

api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()



def GetCursor():
    # Функция возвращает координаты пространства 2D документа

    ActiveDoc = obj5.ActiveDocument2D()
    request_info = obj5.GetParamStruct(constants.ko_RequestInfo)
    result, x, y = ActiveDoc.ksCursor(request_info, 0.0, 0.0, None)
    return x, y, result

def WriteText(x, y, text, angle=0, hStr=3.5):
    # Функция выводит текстовую строку в пространстве 2D документа, по координатам
    # x - координаты по оси x
    # y - координаты по оси y
    # text - текстовая строка для вывода

    ActiveDoc = obj5.ActiveDocument2D()
    ActiveDoc.ksText(x, y, angle, hStr, 1, 0, text)

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

def HyperReference(IndEdited, IndObject, codeFun=-1):
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

    iDrawingText0 = iDrawingTexts.DrawingText(IndObject) # Индекс текстовой метки
    iDrawingText1 = iDrawingTexts.DrawingText(IndEdited) # Индекс текстовой метки
    iText = KAPI7.IText(iDrawingText1)
    iTextLine = iText.TextLine(0) # Индекс строчки
    iTextItem = iTextLine.AddBefore(4)
    iTextItem.ItemType = 0x2000
    iHypertextReferenceParam = KAPI7.IHypertextReferenceParam(iTextItem)
    iHypertextReferenceParam.LinkObject = iDrawingText0
    iHypertextReferenceParam.HypertextType = codeFun
    iHypertextReferenceParam.TextLineIndex = 0
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

def MakeLine(x, y, angle, length=15):
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

def HyperReferenceOnly(IndEdited, IndObject, codeFun=-1):
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

    iDrawingText0 = iDrawingTexts.DrawingText(IndObject) # Индекс текстовой метки
    iDrawingText1 = iDrawingTexts.DrawingText(IndEdited) # Индекс текстовой метки
    iText = KAPI7.IText(iDrawingText1)
    iTextLine = iText.TextLine(0) # Индекс строчки
    iTextItem = iTextLine.TextItem(0)
    iTextItem.ItemType= 0x2000
    iHypertextReferenceParam = KAPI7.IHypertextReferenceParam(iTextItem)
    iHypertextReferenceParam.LinkObject = iDrawingText0
    iHypertextReferenceParam.HypertextType = codeFun
    iHypertextReferenceParam.TextLineIndex = 0
    iTextItem.Update()
    iDrawingText1.Update()
    iDrawingText0.Update()

def AddChar(textObj, str, order):
    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iDrawingTexts = iDrawingContainer.DrawingTexts

    iDrawingText = iDrawingTexts.DrawingText(textObj)  # Индекс текстовой метки
    iText = KAPI7.IText(iDrawingText)
    iTextLine = iText.TextLine(0)  # Индекс строчки
    iTextItem = iTextLine.AddBefore(order)
    iTextItem.Str = str
    iTextItem.Update()
    iDrawingText.Update()
    #print(f'Для {textObj} выполнено {Str}') консольная проверка

def MoveText(textObj, x=None, y=None):
    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    iDrawingTexts = iDrawingContainer.DrawingTexts
    iDrawingText = iDrawingTexts.DrawingText(textObj)
    if x is not None:
        iDrawingText.X = x
        iDrawingText.Update()
    if y is not None:
        iDrawingText.Y = y
        iDrawingText.Update()

def LenghtText(x, y):


    ActiveDoc = obj5.ActiveDocument2D()
    TextObject = ActiveDoc.ksFindObj(x, y, 1)

    return ActiveDoc.ksGetTextLengthFromReference(TextObject)

def GetMacrObjS():
    """
    Функция возвращает указатель на комплекс макроэлементов открытого документа Компас 3D

    """
    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    MacroObjects = iDrawingContainer.MacroObjects
    return MacroObjects

def NumMacrObjS(MacrObjS):
    """
    :param MacrObjS: указатель на комплекс макроэлементов открытого документа Компас 3D
    :return: Количиество макроэлементов открытого документа Компас 3D
    """
    return MacrObjS.Count

def GetMacrObjt(MacrObjS, i):
    """
    :param MacrObjS: указатель на комплекс макроэлементов открытого документа Компас 3D
    :param i: Индекс конкретного макроэлемената
    :return: указаель на макроэлемент
    """
    return MacrObjS.MacroObject(i)

def NameMacrObj(MacroObject):
    """
    :param MacroObject:  указатель на конкретный макроэлемент Компас 3D
    :return: Наименование макроэлемента
    """
    return MacroObject.Name

def HyperProp_txtMark(DrawingText, MacroObject, numOfProp):

    kompas_document = api.ActiveDocument
    iPropertyMng = KAPI7.IPropertyMng(api)
    baseProp = iPropertyMng.GetProperty(kompas_document, numOfProp)
    iPropertyKeeper = KAPI7.IPropertyKeeper(MacroObject)
    iText = KAPI7.IText(DrawingText)
    iTextLine = iText.TextLine(0)  # Индекс строчки
    iTextItem = iTextLine.TextItem(0)
    iTextItem.ItemType = 0x2000
    iHypertextReferenceParam = KAPI7.IHypertextReferenceParam(iTextItem)
    iHypertextReferenceParam.HypertextType = 0x80
    iHypertextReferenceParam.LinkObject = MacroObject
    iHypertextReferenceParam.PropertyId = numOfProp
    iHypertextReferenceParam.TextLineIndex = 0
    iTextItem.Update()
    DrawingText.Update()


def WriteMacroProp(MacroObject, numOfProp, mark):
    """
    :param MacroObject: указатель на конкретный макроэлемент Компас 3D
    :param numOfProp: Номер свойства в параметрах сверху вниз начиная с 0
    :param mark: текстовая метка, которая будет записана в свойство
    :return: успешно прошла операция или нет
    """
    kompas_document = api.ActiveDocument
    iPropertyMng = KAPI7.IPropertyMng(api)
    baseProp = iPropertyMng.GetProperty(kompas_document, numOfProp)
    iPropertyKeeper = KAPI7.IPropertyKeeper(MacroObject)
    return iPropertyKeeper.SetPropertyValue(baseProp, mark, 1)

def GetTxtDraw(MacroObject):
    """
    :param MacroObject: указатель на конкретный макроэлемент Компас 3D
    :return: контейнер текстовой метки
    """
    iView = KAPI7.IView(MacroObject)
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    DrawingTexts = iDrawingContainer.DrawingTexts
    return DrawingTexts.DrawingText(0)


def GetTxtMacro(DrawingText):
    """
    :param MacroObject: указатель на конкретный макроэлемент Компас 3D
    :return:
    """
    iText = KAPI7.IText(DrawingText)
    return iText.Str

def ReplaceTxt(DrawingText,  txt):
    iText = KAPI7.IText(DrawingText)
    iText.Clear()
    iTextLine = iText.Add()  # Индекс строчки
    iTextItem = iTextLine.Add()
    iTextItem.Str = txt
    iTextItem.Update()
    DrawingText.Update()
    return

def HyperProperty(DrawingText, MacroObject, numOfProp = 3, type = -1):

    kompas_document = api.ActiveDocument
    iPropertyMng = KAPI7.IPropertyMng(api)
    baseProp = iPropertyMng.GetProperty(kompas_document, numOfProp)
    iPropertyKeeper = KAPI7.IPropertyKeeper(MacroObject)
    return iPropertyKeeper.InsertHypertextReference(baseProp, DrawingText, type, False, 0, 0, 0)


def Test():
    """
    numOfPror
    Порядковый номер свойства начиная с 0 в шаблоне Компас-3D
    """
    kompas_document = api.ActiveDocument
    kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
    iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
    iViews = iViewsAndLayersManager.Views
    iView = iViews.ActiveView
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    MacroObjects = iDrawingContainer.MacroObjects
    MacroObject = MacroObjects.MacroObject(0)


    MacroObject_Name = MacroObject.Name
    print(MacroObject_Name)

    iView = KAPI7.IView(MacroObject)
    iDrawingContainer = KAPI7.IDrawingContainer(iView)
    DrawingTexts = iDrawingContainer.DrawingTexts
    DrawingText = DrawingTexts.DrawingText(0)
    iText = KAPI7.IText(DrawingText)
    iTextLine = iText.TextLine(0)  # Индекс строчки
    iTextItem = iTextLine.TextItem(0)
    iTextItem.ItemType = 0x2000

    iPropertyMng = KAPI7.IPropertyMng(api)
    baseProp = iPropertyMng.GetProperty(kompas_document, 4)
    idProp = baseProp.Id

    iPropertyKeeper = KAPI7.IPropertyKeeper(MacroObject)

    iHypertextReferenceParam = KAPI7.IHypertextReferenceParam(iTextItem)


    iHypertextReferenceParam.LinkObject = iDrawingContainer
    iHypertextReferenceParam.HypertextType = 0x80
    iHypertextReferenceParam.PropertyId = idProp

    iTextItem.Update()
    DrawingText.Update()







    #iPropertyKeeper.SetPropertyValue(baseProp, 'base', '89898')

    #baseProp.Update()

def GetMacrTEST():
    # Имя свойства
    name = 'Новое свойство'
    # Значение свойства
    value = 100

    # Базовый класс документов КОМПАС
    iKompasDocument = api.ActiveDocument
    # Базовый класс документов-моделей КОМПАС (скрытый)
    kompas_document_2d = KAPI7.IKompasDocument2D(iKompasDocument)
    # Интерфейс компонента 3D документа
    iPropertyMng = KAPI7.IPropertyMng(api)
    # Добавить свойство
    #iProperty = iPropertyMng.AddProperty(iKompasDocument, VARIANT(VT_EMPTY, None))
    iProperty = iPropertyMng.GetProperty(iKompasDocument, 4)
    print(iProperty)
    # Имя свойства
    #iProperty.Name = name
    # Обновить свойство
    #iProperty.Update()
    # Интерфейс получения/редактирования значения свойств
    #iPropertyKeeper = KAPI7.IPropertyKeeper(kompas_document_2d)
    # Установить значение свойства
    #iPropertyKeeper.SetPropertyValue(iProperty, value, 1)



