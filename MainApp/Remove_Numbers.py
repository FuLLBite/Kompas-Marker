from KFunc import GetMacrObjS, NumMacrObjS, NameMacrObj, GetMacrObjt, GetTxtMacro, GetTxtDraw, ReplaceTxt

MacrObjS = GetMacrObjS()
numOfMacro = NumMacrObjS(MacrObjS)

for i in range(numOfMacro):

    MacroObject = GetMacrObjt(MacrObjS, i)
    nameElement = NameMacrObj(MacroObject)
    txtContainer = GetTxtDraw(MacroObject)

    try:
        txtPose = GetTxtMacro(txtContainer)
    except:
        continue

    txt_pose_wout_num = ''
    for k in txtPose:
        if k.isdigit():
            break
        else:
            txt_pose_wout_num += k

    if txtPose != txt_pose_wout_num:
        ReplaceTxt(txtContainer, txt_pose_wout_num)