import pythoncom
from win32com.client import Dispatch, gencache
from Get_Kompas_API import get_kompas_api7


api, KAPI7, api5, KAPI5 = get_kompas_api7()

    # Получаем активный документ (IDocument)
doc = api.ActiveDocument
if doc is None:
    print("Нет активного документа")


    # Приводим к интерфейсу IKompasDocument2D
doc2d = KAPI7.IKompasDocument2D(
    doc._oleobj_.QueryInterface(
        KAPI7.IKompasDocument2D.CLSID,
        pythoncom.IID_IDispatch
        )
    )

# Смотрим что реально есть на IKompasDocument2D
attrs = [a for a in dir(doc2d) if not a.startswith('_')]
methods = [a for a in attrs if callable(getattr(doc2d, a, None))]
props = [a for a in attrs if not callable(getattr(doc2d, a, None))]
print("Методы doc2d:", methods)
print("Свойства doc2d:", props)

# Пробуем IKompasDocument2D1 (расширенный интерфейс)
try:
    doc2d1 = KAPI7.IKompasDocument2D1(
        doc._oleobj_.QueryInterface(
            KAPI7.IKompasDocument2D1.CLSID,
            pythoncom.IID_IDispatch
        )
    )
    attrs1 = [a for a in dir(doc2d1) if not a.startswith('_')]
    print("Атрибуты IKompasDocument2D1:", attrs1)
except Exception as e:
    print("IKompasDocument2D1 недоступен:", e)

# Пробуем через приложение напрямую
try:
    api_attrs = [a for a in dir(api) if 'select' in a.lower() or 'Select' in a]
    print("Selection-атрибуты на IApplication:", api_attrs)
except Exception as e:
    print("Ошибка:", e)
