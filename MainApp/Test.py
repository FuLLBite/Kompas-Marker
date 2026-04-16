import pythoncom
from win32com.client import Dispatch

from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, api5, KAPI5 = get_kompas_api7()
#iDocument = api.ActiveDocument
doc = api.ActiveDocument
doc2d1 = KAPI7.IKompasDocument2D1(
        doc._oleobj_.QueryInterface(
            KAPI7.IKompasDocument2D1.CLSID,
            pythoncom.IID_IDispatch
        )
    )

Document = doc2d1.SelectionManager
iDocument = Document.SelectedObjects

#iDocument = api.ActiveDocument
#iKompasDocument2D1 = iDocument.IKompasDocument()
#iKompasDocument2D1 = iDocument.IKompasDocument2D1()
#SelectionManager = iKompasDocument2D1.SelectionManager
#SelectedObjects = SelectionManager.SelectedObjects
#draft = iKompasDocument2D1.IModelObject.IZone(SelectedObjects)
dir(iDocument)

methods = [m for m in dir(iDocument) if not m.startswith('_') and callable(getattr(iDocument, m, None))]
print("Методы:", methods)

# 3. Фильтр свойств (без скобок)
props = [p for p in dir(iDocument) if not p.startswith('_') and not callable(getattr(iDocument, p, None))]
print("Свойства:", props)

# 4. Тестируем каждый метод с параметрами
for method in methods[:5]:  # Первые 5
    try:
        print(f"{method}: {getattr(iDocument, method).__doc__}")
    except:
        print(f"{method}: требует параметры")

