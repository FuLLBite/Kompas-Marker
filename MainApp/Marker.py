import os
import re
import subprocess
import pythoncom
from win32com.client import Dispatch, gencache
from tkinter.filedialog import askopenfilenames
import LDefin2D


from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, api5, KAPI5 = get_kompas_api7()

iDocument = api.ActiveDocument

#iKompasDocument2D1 = iDocument.IKompasDocument()
#iKompasDocument2D1 = iDocument.IKompasDocument2D1()
#SelectionManager = KAPI7.ISelectionManager
#SelectedObjects = KAPI7.GetSelectedObjects()
#draft = iKompasDocument2D1.IModelObject.IZone(SelectedObjects)
doc2d = KAPI7.IKompasDocument2D(
    iDocument._oleobj_.QueryInterface(
        KAPI7.IKompasDocument2D.CLSID,
        pythoncom.IID_IDispatch
    )
)

# Получаем менеджер выделения
sel_manager = doc2d.SelectionManager

# Получаем коллекцию выделенных объектов
selected = sel_manager.SelectedObjects

count = selected.Count
if count == 0:
    print("Ничего не выделено")

result = []
for i in range(count):
    obj = selected.Item(i)
    result.append(obj)
    print(f"[{i}] Тип: {obj.type}, Стиль: {obj.style}")
