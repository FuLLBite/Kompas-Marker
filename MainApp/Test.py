import pythoncom
from win32com.client import Dispatch
import inspect

from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, api5, KAPI5, obj7 = get_kompas_api7()
Document = api.ActiveDocument
iDocument1 = KAPI7.IKompasDocument2D1(
    Document._oleobj_.QueryInterface(
        KAPI7.IKompasDocument2D1.CLSID,
        pythoncom.IID_IDispatch
    )
)
sel_manager = iDocument1.SelectionManager

# Получаем коллекцию выделенных объектов
iDocument = sel_manager.SelectedObjects
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


