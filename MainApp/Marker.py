import os
import re
import subprocess
import pythoncom
from win32com.client import gencache
from tkinter.filedialog import askopenfilenames
import LDefin2D


from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, api5, KAPI5, obj7 = get_kompas_api7()
constants = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0).constants



#iKompasDocument2D1 = iDocument.IKompasDocument()
#iKompasDocument2D1 = iDocument.IKompasDocument2D1()
#SelectionManager = KAPI7.ISelectionManager
#SelectedObjects = KAPI7.GetSelectedObjects()
#draft = iKompasDocument2D1.IModelObject.IZone(SelectedObjects)

doc2d = api5.ActiveDocument2D()

# Тест до ksCursor
doc2d.ksOpenView(0)
print("ksLineSeg BEFORE cursor:", doc2d.ksLineSeg(10, 10, 60, 60, 1))

request_info = api5.GetParamStruct(constants.ko_RequestInfo)
result, x, y = doc2d.ksCursor(request_info, 0.0, 0.0, None)



if result:
    zona = doc2d.ksGetZona(x, y)
    zone_name = zona[0]
    print(zone_name)

    print("ProcessRunning:", doc2d.ksIsActiveProcessRunnig())
    print("ksOpenView(0):", doc2d.ksOpenView(0))
    print("ksLineSeg test:", doc2d.ksLineSeg(0, 0, 50, 50, 1))

    iParagraphParam = KAPI5.ksParagraphParam(api5.GetParamStruct(constants.ko_ParagraphParam))
    iParagraphParam.Init()
    iParagraphParam.x = x
    iParagraphParam.y = y
    iParagraphParam.ang = 0
    iParagraphParam.height = 7.0
    iParagraphParam.width = 20.0
    iParagraphParam.hFormat = 0
    iParagraphParam.vFormat = 0
    iParagraphParam.style = 1
    print("ksParagraph:", doc2d.ksParagraph(iParagraphParam))

    iTextLineParam = KAPI5.ksTextLineParam(api5.GetParamStruct(constants.ko_TextLineParam))
    iTextLineParam.Init()
    iTextLineParam.style = 1

    iTextItemArray = api5.GetDynamicArray(LDefin2D.TEXT_ITEM_ARR)
    iTextItemParam = KAPI5.ksTextItemParam(api5.GetParamStruct(constants.ko_TextItemParam))
    iTextItemParam.Init()
    iTextItemParam.iSNumb = 0
    iTextItemParam.s = zone_name
    iTextItemParam.type = 0

    iTextItemFont = KAPI5.ksTextItemFont(iTextItemParam.GetItemFont())
    iTextItemFont.Init()
    iTextItemFont.bitVector = 4096
    iTextItemFont.color = 0
    iTextItemFont.fontName = "GOST type A"
    iTextItemFont.height = 5
    iTextItemFont.ksu = 1

    iTextItemArray.ksAddArrayItem(-1, iTextItemParam)
    iTextLineParam.SetTextItemArr(iTextItemArray)
    print("ksTextLine:", doc2d.ksTextLine(iTextLineParam))
    print("ksEndObj:", doc2d.ksEndObj())
    print("ksReturnResult:", api5.ksReturnResult())
    print("ksStrResult:", api5.ksStrResult())

    doc2d.ksRebuildDocument()