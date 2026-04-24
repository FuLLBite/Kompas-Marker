import pythoncom
from win32com.client import Dispatch, gencache
from Test import Help
import LDefin2D

const = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
#  Подключим константы API Компас
kompas6_constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants
kompas6_constants_3d = gencache.EnsureModule("{2CAF168C-7961-4B90-9DA2-701419BEEFE3}", 0, 1, 0).constants

#  Подключим описание интерфейсов API5
kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
kompas_object = kompas6_api5_module.KompasObject(Dispatch("Kompas.Application.5")._oleobj_.QueryInterface(kompas6_api5_module.KompasObject.CLSID, pythoncom.IID_IDispatch))


#  Подключим описание интерфейсов API7
kompas_api7_module = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)
application = kompas_api7_module.IApplication(Dispatch("Kompas.Application.7")._oleobj_.QueryInterface(kompas_api7_module.IApplication.CLSID, pythoncom.IID_IDispatch))



Documents = application.Documents
#  Получим активный документ
kompas_document = application.ActiveDocument
kompas_document_2d = kompas_api7_module.IKompasDocument2D(kompas_document)
kompas_document_2d1 = kompas_api7_module.IKompasDocument2D1(kompas_document_2d)
iDocument2D = kompas_object.ActiveDocument2D()

#Help(kompas_document_2d)

obj = iDocument2D.ksArcByPoint(391.764239119426, 147.551012715639, 100, 251.682230149398, 180.913128399765, 488.459001860047, 254.256789778247, -1, 14)

#API5
iEllipseParam = kompas6_api5_module.ksEllipseParam(kompas_object.GetParamStruct(const.ko_EllipseParam))
iEllipseParam.Init()
iEllipseParam.xc = 100
iEllipseParam.yc = 150
iEllipseParam.A = 20
iEllipseParam.B = 40
iEllipseParam.style = 1
#obj = iDocument2D.ksEllipse(iEllipseParam)

#API7
iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
iViews = iViewsAndLayersManager.Views
iView = iViews.ActiveView
iDrawingContainer = kompas_api7_module.IDrawingContainer(iView)
iEllipses = iDrawingContainer.Ellipses
iEllipse = iEllipses.Add()
iEllipse.Xc = 100
iEllipse.Yc = 150
iEllipse.SemiAxisA = 20
iEllipse.SemiAxisB = 40
iEllipse.Style = 1
iEllipse.Update()