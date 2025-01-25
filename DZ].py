import numpy as np
import pandas as pd

# 1. Привести различные способы создания объектов типа Series
# Для создания Series можно использовать
# - списки Python или массивы NumPy
lista = np.array([1,2,3,4])
listb = np.array([5,6,7,8])
data = pd.Series(lista,index=listb)
# - скалярные значение
data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
# - словари
dicta = {1:10,2:20,3:30}
data = pd.Series(dicta)

# 2. Привести различные способы создания объектов типа DataFrame
# DataFrame. Способы создания
# - через объекты Series
dataa = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
datab = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
frame = pd.DataFrame({'one':dataa,'two':datab})
# - списки словарей
dicta = {1:10,2:20,3:30}
dictb = {1:10,2:20,3:30}
listdict = [dicta,dictb]
frame = pd.DataFrame(listdict)
# - словари объектов Series
#dictofser = {dataa:datab}
#frame = pd.DataFrame([dicta])
# - двумерный массив NumPy
mas = [[1,2,3],[4,5,6]]
frame = pd.DataFrame(mas)
# - структурированный массив Numpy
structured = np.array([(1,  0.5, 1+2j),(2, 1.3, 2-2j), (3,  0.8, 1+3j)], dtype=('i2, f4, c8'))
frame = pd.DataFrame(structured)

# 3. Объедините два объекта Series с неодинаковыми множествами ключей (индексов) так, чтобы вместо NaN было установлено значение 1
pop = pd.Series({
    'city_1':1000,
    'city_2':2000,
    'city_3':3000,
    'city_4':4000,
    'city_5':5000
})


area = pd.Series({
    'city_1':100,
    'city_2':200,
    'city_3':300,
    'city_42':400,
    'city_52':500
})

data = pd.DataFrame({'area1':area,'pop1':pop}).fillna(1)
print(data)
# 4. Переписать пример с транслирование для DataFrame так, чтобы вычитание происходило по СТОЛБЦАМ
df.sub(df.f,axis=0)
# 5. На примере объектов DataFrame продемонстрируйте использование методов ffill() и bfill()
data = pd.DataFrame({'area1':area,'pop1':pop}).ffill()
print(data)
data = pd.DataFrame({'area1':area,'pop1':pop}).bfill()
print(data)