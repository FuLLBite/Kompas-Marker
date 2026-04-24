import pythoncom
from win32com.client import Dispatch

from Get_Kompas_API import get_kompas_api7

def Help(iDocument):

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


