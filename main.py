import numpy as np
import pandas as pd

# v pandas mozhno indeksirovat ne tolko chislami

#osn struct - series, DataFrame, Index

data = pd.Series([0.25,0.5,0.75,1.0])
print(data)
print(type(data))

print(data.values)
print(data.index)

print(data[0])
print(data[1:3])

data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
print(data)
print(data['a'])
print(data['b':'d'])

data = pd.Series([0.25,0.5,0.75,1.0],index=[1,7,10,'d'])
print(data)
print(data[1])
print(data[7:'d'])

population_dict = {
    'city_1':1000,
    'city_2':2000,
    'city_3':3000,
    'city_4':4000,
    'city_5':5000
}

population = pd.Series(population_dict)

print(population['city_4'])
print(population['city_4':'city_5'])


#DataFrame - 2d massive s opr indexami, soglassovannie po indexas seriesi

population_dict = {
    'city_1':1000,
    'city_2':2000,
    'city_3':3000,
    'city_4':4000,
    'city_5':5000
}
population = pd.Series(population_dict)

area_dict = {
    'city_1':100,
    'city_2':200,
    'city_3':300,
    'city_4':400,
    'city_5':500
}
area = pd.Series(area_dict)

states = pd.DataFrame({
    'population1':population,
    'area1':area
})

print(states)
print(states.index)
print(states.columns)

print(type(states.values))
print(type(states.index))
print(type(states.columns))

print(states['area1'])

#sozdat mozhno cherez series, list of dict, dict of series, 2d np array, structed massive numpy

#index - can not change, sorted, multimnozhestvo(povtor znach)

ind = pd.Index([2,3,5,7,11])
print(ind[1])
print(ind[::2])

indA = pd.Index([1,2,3,4,5])
indB = pd.Index([6,7,8,9,1])

print(indA.intersection(indB))

data = pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])

print('a' in data)
print('z' in data)

print(data.keys())

print(list(data.items()))

data['a'] = 100
data['z'] = 1000

print(data['a':'c'])
print(data[0:2])
print(data[(data>0.5)&(data<1)])
#print(data['a','d'])

#atributi - indexatori

print(data.loc(1))
print(data.iloc(1))

pop = pd.series({
    'city_1':1000,
    'city_2':2000,
    'city_3':3000,
    'city_4':4000,
    'city_5':5000
})


area = pd.series({
    'city_1':100,
    'city_2':200,
    'city_3':300,
    'city_4':400,
    'city_5':500
})
area = pd.DataFrame({'area':area,'pop':pop})

print(data)
print(data['area1'])
print(data.area1)

print(data.pop1 is data['pop1'])

data['new'] = data['area1']


data['new1'] = data['area1']/data['pop1']

print(data)

#2d numpy massiv, udobniy dlya drugih rabot

data = pd.DataFrame({'area1':area, 'pop1':pop, 'pop':pop})

print(data)
print(data.iloc[:3,1:2])
print(data.loc[:'city4','pop1':pop])
print(data.loc[data['pop']>1002,['area1','pop']])

rng = np.random.default_rng()
s = pd.Series(rng.integers(0,10,4))

print(s)
print(np.exp(s))

pop = pd.series({
    'city_1':1000,
    'city_2':2000,
    'city_3':3000,
    'city_4':4000,
    'city_5':5000
})


area = pd.series({
    'city_1':100,
    'city_2':200,
    'city_3':300,
    'city_42':400,
    'city_52':500
})

data = pd.DataFrame({'area1':area, 'pop1':pop})

dfA = pd.DataFrame(rng.integers(0,10,(2,2)),columns=['a','b'])

dfB = pd.DataFrame(rng.integers(0,10,(3,3)),columns=['a','b','c'])

print(dfA + dfB)

rng = np.random.default_rng(1)

A = rng.integers(0,10,(3,4))
print(A)

print(A[0])
print(A - A[0])

df = pd.DataFrame(A,columns=['a','b','c','d'])
print(df)

print(df.iloc[0])

print(df - df.iloc[0])

print(df.iloc[0,::2])

print(df - df.iloc[0,::2])

#NAN - not a number
#NA - znachenia

#dva sposoba chranenia otsut znach
#1) indikatori Nan ili none
#2) null

val1 = np.array([1,2,3,np.none])
print(val1.Nansum(val1))

x = pd.Series(range(10),dtype=int)
x[0] = None
x[1] = np.nan

x2 = pd.Series([1,2,3,np.nan,None,pd.NA])
x3= pd.Series([1,2,3,np.nan,None,pd.NA],dtype='Int32')

print(x3.isnull())
print(x3[x3.isnull()])
print(x3[x3.notnull()])

print(x3.dropna())
df = pd.DataFrame(
    [
        [1,2,3,np.nan,None,pd.NA],
        [1,2,3,4,5,6]
        [1,np.nan,3,4,np.nan,6]
    ]
)
print(df)
print(df.dropna())
print(df.dropna(axis=0))
print(df.dropna(axis=1))

print(df.dropna(axis=1,how='all'))
print(df.dropna(axis=1,how='any'))
print(df.dropna(axis=1,thresh=2))