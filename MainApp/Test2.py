import pythoncom
from Get_Kompas_API import get_kompas_api7

api, KAPI7, api5, KAPI5, obj7 = get_kompas_api7()

iDocument = api.ActiveDocument
doc2d = KAPI7.IKompasDocument2D1(
    iDocument._oleobj_.QueryInterface(
        KAPI7.IKompasDocument2D1.CLSID,
        pythoncom.IID_IDispatch
    )
)

sel_manager = doc2d.SelectionManager
macro_obj = sel_manager.SelectedObjects

print("Тип объекта:", type(macro_obj))
print()

# Все атрибуты
all_attrs = [a for a in dir(macro_obj) if not a.startswith('_')]
methods = [a for a in all_attrs if callable(getattr(macro_obj, a, None))]
props   = [a for a in all_attrs if not callable(getattr(macro_obj, a, None))]

print("Методы:", methods)
print()
print("Свойства и их значения:")
for p in props:
    try:
        print(f"  {p} = {getattr(macro_obj, p)}")
    except Exception as e:
        print(f"  {p} = ОШИБКА: {e}")

print()
print("--- Позиция макроэлемента (GetPlacement) ---")
try:
    placement = macro_obj.GetPlacement()
    print(f"  Placement: {placement}")
    print(f"  Тип: {type(placement)}")
    placement_attrs = [a for a in dir(placement) if not a.startswith('_')]
    print(f"  Атрибуты: {placement_attrs}")
    for a in placement_attrs:
        try:
            print(f"    {a} = {getattr(placement, a)}")
        except:
            pass
except Exception as e:
    print(f"GetPlacement ошибка: {e}")

x, y = 65.0, -137.0  # из GetPlacement

print()
print("--- IKompasDocument2D: DocumentFrames ---")
try:
    doc2d_base = KAPI7.IKompasDocument2D(
        iDocument._oleobj_.QueryInterface(
            KAPI7.IKompasDocument2D.CLSID,
            pythoncom.IID_IDispatch
        )
    )

    frames = doc2d_base.DocumentFrames
    print(f"  DocumentFrames = {frames}")
    print(f"  Тип: {type(frames)}")
    if frames is not None:
        frame_attrs = [a for a in dir(frames) if not a.startswith('_')]
        print(f"  Атрибуты: {frame_attrs}")
        for a in frame_attrs:
            if not callable(getattr(frames, a, None)):
                try:
                    print(f"    {a} = {getattr(frames, a)}")
                except Exception as e:
                    print(f"    {a} = ОШИБКА: {e}")
except Exception as e:
    print(f"DocumentFrames ошибка: {e}")

ref = macro_obj.Reference
doc5 = api5.ActiveDocument2D()

print()
print("--- ksOpenMacro ---")
try:
    result = doc5.ksOpenMacro(ref)
    print(f"  ksOpenMacro = {result}")
except Exception as e:
    print(f"  ksOpenMacro ошибка: {e}")

print()
print("--- GetSpecification на doc5 ---")
try:
    spec = doc5.GetSpecification()
    print(f"  spec = {spec}, тип = {type(spec)}")
    if spec is not None:
        spec_attrs = [a for a in dir(spec) if not a.startswith('_')]
        print(f"  Методы/свойства: {spec_attrs}")
except Exception as e:
    print(f"  GetSpecification ошибка: {e}")

print()
print("--- SpecificationDescriptions на doc2d_base ---")
try:
    spc_desc = doc2d_base.SpecificationDescriptions
    print(f"  SpecificationDescriptions = {spc_desc}, тип = {type(spc_desc)}")
    if spc_desc is not None:
        attrs = [a for a in dir(spc_desc) if not a.startswith('_')]
        print(f"  Атрибуты: {attrs}")
        if hasattr(spc_desc, 'Count'):
            print(f"  Count = {spc_desc.Count}")
except Exception as e:
    print(f"  SpecificationDescriptions ошибка: {e}")

print()
print("--- ksGetMacroPlacementEx ---")
try:
    result = doc5.ksGetMacroPlacementEx(ref)
    print(f"  ksGetMacroPlacementEx = {result}")
    print(f"  тип = {type(result)}")
except Exception as e:
    print(f"  ksGetMacroPlacementEx ошибка: {e}")

print()
print("--- DocumentFrames.Item(0) ---")
try:
    frame = doc2d_base.DocumentFrames.Item(0)
    print(f"  frame тип = {type(frame)}")
    if frame is not None:
        attrs = [a for a in dir(frame) if not a.startswith('_')]
        print(f"  Методы: {[a for a in attrs if callable(getattr(frame, a, None))]}")
        for p in [a for a in attrs if not callable(getattr(frame, a, None))]:
            try:
                print(f"    {p} = {getattr(frame, p)}")
            except Exception as e:
                print(f"    {p} = ОШИБКА: {e}")
    else:
        print("  Item(0) тоже None")
except Exception as e:
    print(f"Item(0) ошибка: {e}")

print()
print("--- API5: doc5 свойства ---")
try:
    doc5 = api5.ActiveDocument2D()
    print(f"  doc5 тип = {type(doc5)}")
    attrs5 = [a for a in dir(doc5) if not a.startswith('_')]
    zone_related = [a for a in attrs5 if 'zone' in a.lower() or 'зон' in a.lower()
                    or 'stamp' in a.lower() or 'frame' in a.lower() or 'format' in a.lower()]
    print(f"  Зона/штамп/формат атрибуты: {zone_related}")
    print(f"  Все методы: {[a for a in attrs5 if callable(getattr(doc5, a, None))]}")
except Exception as e:
    print(f"API5 doc5 ошибка: {e}")