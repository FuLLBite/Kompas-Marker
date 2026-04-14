import os
import re
import subprocess
import pythoncom
from win32com.client import Dispatch, gencache
from tkinter.filedialog import askopenfilenames
import LDefin2D


from Get_Kompas_API import get_kompas_api7

#def marker():
api, KAPI7 = get_kompas_api7()
iDocument = api.ActiveDocument
iKompasDocument2D1 = iDocument.IKompasDocument2D1()
#SelectionManager = iKompasDocument2D1.SelectionManager
#SelectedObjects = SelectionManager.SelectedObjects
#draft = iKompasDocument2D1.IModelObject.IZone(SelectedObjects)

print(iDocument)