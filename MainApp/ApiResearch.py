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
MacroObjects = iDrawingContainer.MacroObjects
MacroObject = MacroObjects.MacroObject(1)
iApplication = KAPI7.IApplication(MacroObject)
iPropertyMng = KAPI7.IPropertyMng(iApplication)

iDocument = iPropertyMng


dir(iDocument)

methods = [m for m in dir(iDocument) if not m.startswith('_') and callable(getattr(iDocument, m, None))]
print("Методы:\n", *methods, sep='\n')

# 3. Фильтр свойств (без скобок)
props = [p for p in dir(iDocument) if not p.startswith('_') and not callable(getattr(iDocument, p, None))]
print("\nСвойства:\n", *props, sep='\n')

interfaces = [
    name for name, obj in inspect.getmembers(KAPI7)
    if inspect.isclass(obj) and hasattr(obj, 'CLSID')
    ]
print("\nИнтерфейсы KAPI7:\n", *interfaces, sep='\n')

# 6. Список доступных интерфейсов из модуля KAPI5
interfaces5 = [
    name for name, obj in inspect.getmembers(KAPI5)
    if inspect.isclass(obj) and hasattr(obj, 'CLSID')
]
print("\nИнтерфейсы KAPI5:\n", *interfaces5, sep='\n')

# 4. Тестируем каждый метод с параметрами
for method in methods[:5]:  # Первые 5
    try:
        print(f"{method}: {getattr(iDocument, method).__doc__}")
    except:
        print(f"{method}: требует параметры")

