from win32com.client import Dispatch, gencache
from Get_Kompas_API import get_kompas_api7




def GetCursor():

    api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()
    ActiveDoc = obj5.ActiveDocument2D()

    request_info = obj5.GetParamStruct(constants.ko_RequestInfo)
    result, x, y = ActiveDoc.ksCursor(request_info, 0.0, 0.0, None)

    return x, y



def WriteText():
    api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()
    ActiveDoc = obj5.ActiveDocument2D()
    ActiveDoc.ksText(100, 100, 0, 5, 1, 0, 'TYR')

