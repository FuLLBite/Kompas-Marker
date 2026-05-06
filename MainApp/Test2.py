import pythoncom
from win32com.client import Dispatch, gencache

# Генерация модулей API (выполнить ОДИН РАЗ при первом запуске)
print("Генерация модулей API...")
kapi7_module = gencache.EnsureModule("{69AC2981-37C0-4379-84FD-5DD2F3C0A520}", 0, 1, 0)  # API7
kconst_module = gencache.EnsureModule("{75C9F5D0-B5B8-4526-8681-9903C567D2ED}", 0, 1, 0)  # Константы
constants = kconst_module.constants
print("Модули API сгенерированы.")

def InsertText(ref, x, y):
    """
    ref: Reference из API5 (int/long)
    x, y: координаты текста (float)
    Создает гипертекст "K(номер листа,зона)"
    """
    pythoncom.CoInitialize()

    try:
        # Подключение к Kompas API7
        kompas_app = Dispatch("Kompas.Application.7")
        kompas_app.Visible = True
        kobj = kapi7_module.IKompasAPIObject(kompas_app)
        print("Подключен к Kompas API7")

        # Получить контейнер графических объектов (IDrawingContainer)
        pDrawingContainer = kobj.GetDrawingContainer()
        if pDrawingContainer is None:
            print("Ошибка: Нет IDrawingContainer (откройте чертеж!)")
            return False

        print("Получен IDrawingContainer")

        # Создать блок текста (IDrawingText)
        pDrawingTexts = pDrawingContainer.DrawingTexts
        pDrawingText = pDrawingTexts.Add()

        # Настройки блока текста
        pDrawingText.Allocation = constants.ksAlCentre  # По центру
        pDrawingText.Angle = 0
        pDrawingText.Height = 10
        pDrawingText.Width = 50
        pDrawingText.HFormat = constants.ksHFormatNot
        pDrawingText.VFormat = False
        pDrawingText.X = x - 20
        pDrawingText.Y = y

        # Получить интерфейс IText
        pText = pDrawingText.QueryInterface(kapi7_module.IText)
        if pText is None:
            print("Ошибка: Не удалось получить IText")
            return False

        print("Создан IText")

        # TransferReference: ref из API5 → API7
        current_doc = kobj.ksGetCurrentDocument(0)
        transferred_kobj = kobj.TransferReference(ref, current_doc)
        if transferred_kobj is None:
            print("Ошибка: TransferReference вернул None (неверный ref)")
            return False

        print("TransferReference выполнен")

        # Строка 1: 'K'
        pTextLine1 = pText.Add()
        pTextLine1.Align = constants.ksAlignCenter
        pTextLine1.Str = 'K'

        # Строка 2: "(лист,зона)"
        pTextLine2 = pText.Add()
        pTextLine2.Align = constants.ksAlignCenter

        # 1. '(' - обычный текст
        pTextItem1 = pTextLine2.Add()
        pTextItem1.Str = '('
        pTextItem1.ItemType = constants.ksTItString
        pTextItem1.Update()

        # 2. Гиперссылка: Номер листа (ksHTObjectSheet)
        pTextLine2.InsertHyperTextReference(1, transferred_kobj, constants.ksHTObjectSheet, False, 0, 0, 0)

        # 3. ','
        pTextItem2 = pTextLine2.Add()
        pTextItem2.Str = ','
        pTextItem2.ItemType = constants.ksTItString
        pTextItem2.Update()

        # 4. Гиперссылка: Обозначение зоны (ksHTObjectZone)
        pTextLine2.InsertHyperTextReference(1, transferred_kobj, constants.ksHTObjectZone, False, 0, 0, 0)

        # 5. ')'
        pTextItem3 = pTextLine2.Add()
        pTextItem3.Str = ')'
        pTextItem3.ItemType = constants.ksTItString
        pTextItem3.Update()

        # Обновить блок текста
        pDrawingText.Update()
        print("✓ Текст 'K(лист,зона)' успешно вставлен в позицию ({:.1f}, {:.1f})".format(x-20, y))
        return True

    except Exception as e:
        print(f"Ошибка: {e}")
        return False
    finally:
        pythoncom.CoUninitialize()

# Тестирование
if __name__ == "__main__":
    # Замените ref на реальный Reference из вашего кода!
    result = InsertText(ref=12345, x=100.0, y=200.0)  # ref должен быть валидным!
    if result:
        print("Скрипт выполнен успешно!")
    else:
        print("Скрипт завершился с ошибкой. Проверьте:")
        print("- Kompas запущен с открытым чертежом")
        print("- ref - валидный Reference из текущего документа")
        print("- pywin32 установлен: pip install pywin32")