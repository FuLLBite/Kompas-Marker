import os
import re
import subprocess
import pythoncom
from win32com.client import Dispatch, gencache
from tkinter.filedialog import askopenfilenames
import LDefin2D


from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7, api5, KAPI5 = get_kompas_api7()

#iDocument = api.ActiveDocument

#iKompasDocument2D1 = iDocument.IKompasDocument()
#iKompasDocument2D1 = iDocument.IKompasDocument2D1()
#SelectionManager = KAPI7.ISelectionManager
#SelectedObjects = KAPI7.GetSelectedObjects()
#draft = iKompasDocument2D1.IModelObject.IZone(SelectedObjects)
doc = api.ActiveDocument
doc2d1 = KAPI7.IKompasDocument2D1(
        doc._oleobj_.QueryInterface(
            KAPI7.IKompasDocument2D1.CLSID,
            pythoncom.IID_IDispatch
        )
    )

Document = doc2d1.SelectionManager
iObject = Document.SelectedObjects
Param = iObject.DrawingObjectParamType
print(iObject)