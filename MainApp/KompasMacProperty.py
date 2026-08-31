from KFunc import GetMacrObjS, NumMacrObjS, NameMacrObj, GetMacrObjt, GetTxtMacro, WriteMacroProp, GetTxtDraw, HyperProperty, HyperProp_txtMark


MacrObjS = GetMacrObjS()

numOfElements = {}
numOfMacro = NumMacrObjS(MacrObjS)

for i in range(numOfMacro):
    MacroObject = GetMacrObjt(MacrObjS, i)
    nameElement = NameMacrObj(MacroObject)
    txtContainer = GetTxtDraw(MacroObject)
    txtPose = GetTxtMacro(txtContainer)
    if nameElement not in numOfElements:
        numOfElements[nameElement] = 1
    else:
        numOfElements[nameElement] += 1
    WriteMacroProp(MacroObject, 4, txtPose + str(numOfElements[nameElement]))
    HyperProperty(txtContainer, MacroObject)


print(numOfElements)