import pythoncom
from win32com.client import Dispatch, gencache
from Get_Kompas_API import get_kompas_api7


def get_selected_objects():
    api, KAPI7, api5, KAPI5 = get_kompas_api7()

    doc = api.ActiveDocument
    if doc is None:
        print("Нет активного документа")
        return []

    # Используем IKompasDocument2D1 — именно он содержит SelectionManager
    doc2d1 = KAPI7.IKompasDocument2D1(
        doc._oleobj_.QueryInterface(
            KAPI7.IKompasDocument2D1.CLSID,
            pythoncom.IID_IDispatch
        )
    )

    sel_manager = doc2d1.SelectionManager

    attrs = [a for a in dir(sel_manager) if not a.startswith('_')]
    methods = [a for a in attrs if callable(getattr(sel_manager, a, None))]
    props = [a for a in attrs if not callable(getattr(sel_manager, a, None))]
    print("Методы sel_manager:", methods)
    print("Свойства sel_manager:", props)

    return []


if __name__ == "__main__":
    objects = get_selected_objects()
    print(f"Выделено объектов: {len(objects)}")