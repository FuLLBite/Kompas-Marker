import pythoncom
from win32com.client import Dispatch

pythoncom.CoInitialize()

# Базовое подключение БЕЗ gencache
app_raw = Dispatch("Kompas.Application.7")
print(f"КОМПАС подключен: {app_raw}")
print(f"Видимость: {app_raw.Visible}")
print(f"Количество документов: {app_raw.Documents.Count}")

# Попытка получить ActiveDocument
try:
    doc = app_raw.ActiveDocument
    print(f"ActiveDocument: {doc}")
    if doc:
        print(f"Имя документа: {doc.Name}")
        print(f"Тип: {doc.DocumentType}")
        print(f"Путь: {doc.PathName}")
    else:
        print("ActiveDocument = None")
except Exception as e:
    print(f"Ошибка ActiveDocument: {e}")


doc = app_raw.Documents
if app_raw.Count > 0:
    # Делаем первый документ активным
    first_doc = doc.Item(0)
    first_doc.Activate()  # ← Активируем!
    doc = doc.ActiveDocument
    print("После активации:", doc)
pythoncom.CoUninitialize()

