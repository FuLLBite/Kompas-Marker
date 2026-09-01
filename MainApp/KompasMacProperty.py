
from KFunc import (GetMacrObjS,
                   NumMacrObjS,
                   NameMacrObj,
                   GetMacrObjt,
                   GetTxtMacro,
                   WriteMacroProp,
                   GetTxtDraw,
                   HyperProperty,
                   ReplaceTxt,
                   GetTxtDraws,
                   Count)


MacrObjS = GetMacrObjS() # Вызов указателя, который содержит все макроэлементы вида
numOfMacro = NumMacrObjS(MacrObjS) # количество макроэлементов

def SetMacroProp():
    mac_objts = GetMacroInfo()  # Вызов структуры данных макроэлемента
    for pos in mac_objts:  # цикл по позиционным обозначениям МЭ
        indeX = 1  # порядковый номер обозначения
        for name in mac_objts[pos]:  # цикл по наименованию МЭ
            for obj in mac_objts[pos][name]:  # цикл по МЭ
                num_pos = pos + str(indeX)  # формирование поз.обозначения для конкретного МЭ
                WriteMacroProp(obj['Макроэлемент'], 4, num_pos)  # Запись в свойства МЭ его поз.обозначеиня
                HyperProperty(obj['Контейнер'], obj['Макроэлемент'])  # Вствка ссылки на зону, тектовой метки МЭ
                ReplaceTxt(obj['Контейнер'], num_pos)  # Обновление поз.обозначения в текстовой метке
                indeX += 1

def GetMacroInfo():
    # сбор информации и формирование структуры данных
    mac_objts = {}
    for i in range(numOfMacro):
        MacroObject = GetMacrObjt(MacrObjS, i)
        nameElement = NameMacrObj(MacroObject)
        pos_name, pos_container = PreparePositionTxT(MacroObject)
        if pos_name is None:
            continue
        mac_objts.setdefault(pos_name, {}).setdefault(nameElement, []).append({'Макроэлемент': MacroObject, 'Контейнер':pos_container})
    return mac_objts

def PreparePositionTxT(MacroObject):
    txtContainers = GetTxtDraws(MacroObject)
    pos_container = None
    pos_name = None
    for i in range(Count(txtContainers)):
        txtContainer = GetTxtDraw(txtContainers, i)
        try:
            txt = GetTxtMacro(txtContainer)
        except:
            continue
        if not txt:
            continue
        if txt[0].isdigit():
            continue

        pos_name = cliningPos(txt)
        pos_container = txtContainer

        if not pos_name or pos_container is None:
            continue

        if pos_name != txt:
            ReplaceTxt(txtContainer, pos_name)

    return pos_name, pos_container

def cliningPos(txt):
    txt_pos_wout_num = ''
    for k in txt:
        if k.isdigit():
            return txt_pos_wout_num
        else:
            txt_pos_wout_num += k
    return txt_pos_wout_num








