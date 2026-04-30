
import KFunc


# Получение координат первой точки
Fx, Fy = KFunc.GetCursor()
# Получение координат второй точки
Sx, Sy = KFunc.GetCursor()

kp = 3 # коэффициент поправки расположения
# Вывод текстовой строки с обозначение зоны
KFunc.WriteText(Fx - kp, Fy - kp, KFunc.GetZona(Sx, Sy))
KFunc.WriteText(Sx - kp, Sy - kp, KFunc.GetZona(Fx, Fy))