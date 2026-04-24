from Get_Kompas_API import get_kompas_api7
import pythoncom

api7, KAPI7, Kobj, KAPI5, const = get_kompas_api7()

def API5():
    # API5
    ksDocument = Kobj.ActiveDocument2D()
    EllipseParam = KAPI5.ksEllipseParam(Kobj.GetParamStruct(const.ko_EllipseParam))
    EllipseParam.Init()
    EllipseParam.xc = 100
    EllipseParam.yc = 150
    EllipseParam.A = 20
    EllipseParam.B = 40
    EllipseParam.style = 1
    EllipseObj = ksDocument.ksEllipse(EllipseParam)

def API7():
    # API7
