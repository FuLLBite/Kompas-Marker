import pythoncom
from win32com.client import Dispatch
import inspect

from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, obj5, KAPI5, obj7, constants = get_kompas_api7()

kompas_document = api.ActiveDocument
kompas_document_2d = KAPI7.IKompasDocument2D(kompas_document)
iViewsAndLayersManager = kompas_document_2d.ViewsAndLayersManager
iViews = iViewsAndLayersManager.Views
iView = iViews.ActiveView
iDrawingContainer = KAPI7.IDrawingContainer(iView)
iDocument = iDrawingContainer.DrawingTexts

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

interfaces = [
    name for name, obj in inspect.getmembers(KAPI7)
    if inspect.isclass(obj) and hasattr(obj, 'CLSID')
    ]
print("\nИнтерфейсы KAPI7:", interfaces)

# 6. Список доступных интерфейсов из модуля KAPI5
interfaces5 = [
    name for name, obj in inspect.getmembers(KAPI5)
    if inspect.isclass(obj) and hasattr(obj, 'CLSID')
]
print("\nИнтерфейсы KAPI5:", interfaces5)

# 4. Тестируем каждый метод с параметрами
for method in methods[:5]:  # Первые 5
    try:
        print(f"{method}: {getattr(iDocument, method).__doc__}")
    except:
        print(f"{method}: требует параметры")


