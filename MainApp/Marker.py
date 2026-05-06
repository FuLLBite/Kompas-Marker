import KFunc

# Получение координат первой точки
Fx, Fy = KFunc.GetCursor()
# Получение координат второй точки
Sx, Sy = KFunc.GetCursor()

quantityTexts = KFunc.CountTexts()

kp = 3 # коэффициент поправки расположения

# Вывод текстовой строки с обозначение зоны
KFunc.WriteText(Fx - kp, Fy - kp, KFunc.GetZona(Sx, Sy))
KFunc.WriteText(Sx - kp, Sy - kp, KFunc.GetZona(Fx, Fy))

# Связывание локальными ссылками тектовые метки
KFunc.HyperReference(quantityTexts, quantityTexts+1)
KFunc.HyperReference(quantityTexts+1, quantityTexts)

# Связывание тектовых меток гиперссылками
KFunc.HyperLink(quantityTexts, quantityTexts+1)
KFunc.HyperLink(quantityTexts+1, quantityTexts)