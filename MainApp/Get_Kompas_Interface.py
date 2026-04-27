import pythoncom
import subprocess
from win32com.client import Dispatch, gencache


kompas6_api5_module = gencache.EnsureModule("{0422828C-F174-495E-AC5D-D31014DBBE87}", 0, 1, 0)
com_kompas = Dispatch("KOMPAS.Application.5")
kompas_object = kompas6_api5_module.KompasObject(
    Dispatch("KOMPAS.Application.5")._oleobj_.QueryInterface(
        kompas6_api5_module.KompasObject.CLSID,
        pythoncom.IID_IDispatch
    )
)

