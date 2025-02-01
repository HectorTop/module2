import numpy as np
import pandas as pd

# esli razmernost >2 use ierarchic indexation (multyindex). V odnom indexze neskolko urovnei

index = [
    ('city_1',2010),
    ('city_1',2020),
    ('city_2',2010),
    ('city_2',2020),
    ('city_3',2010),
    ('city_3',2020)
]

population = [
    101,
    201,
    102,
    202,
    103,
    203
]

pop = pd.Series(population,index = index)

print(pop)

#print(pop[[i for i in pop.index if i[1] == 2020]])

index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)
print(pop)

print(pop[:,2020])
pop_df=pop.unstack()
print(pop_df)
print(pop_df.stack())

index = [
    ('city_1',2010,1),
    ('city_1',2010,2),
    ('city_1',2020,1),
    ('city_1',2020,2),
    ('city_2',2010,1),
    ('city_2', 2010,2),
    ('city_2',2020,1),
    ('city_2', 2020,2),
    ('city_3',2010,1),
    ('city_3', 2010,2),
    ('city_3',2020,1),
    ('city_3',2020,2)
]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030
]

pop = pd.Series(population,index = index)
print(pop)
index = pd.MultiIndex.from_tuples(index)
pop = pop.reindex(index)
print(pop)
print(pop[:,2010])
pop_df = pop.unstack()
print(pop_df)
print(pop_df.stack())

index = [
    ('city_1',2010,1),
    ('city_1',2010,2),
    ('city_1',2020,1),
    ('city_1',2020,2),
    ('city_2',2010,1),
    ('city_2', 2010,2),
    ('city_2',2020,1),
    ('city_2', 2020,2),
    ('city_3',2010,1),
    ('city_3', 2010,2),
    ('city_3',2020,1),
    ('city_3',2020,2)
]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030
]
pop = pd.Series(population,index = index)
print(pop)
index = pd.MultiIndex.from_tuples(index)
pop_df = pd.DataFrame(
    {
        'total':pop,
        'something':[
            10,
            11,
            21,
            21,
            12,
            12,
            22,
            22,
            13,
            13,
            23,
            23
        ]
    }
)
print(pop_df)

print(pop_df['something'])

#pop_df_1 = pop_df.loc['city_1','something']
#print(pop_df_1)

#kak ispolzovat multiindex
#1 - spisok massiva,zadaushich index na kazhdom urovne

i1 = pd.MultiIndex.from_arrays(
    [
        ['a','b','c','d'],
        [1,2,3,4]
    ]
)

#2 - spisok kortezhey,zadaushich znacheniye indexa

i2 = pd.MultiIndex.from_tuples(
    [
        ('a',1),
        ('b',2),
        ('c',3),
        ('d',4)
    ]
)

#3 - cherez dekartovo proizvedeniye

i3 = pd.MultiIndex.from_product(
    [
        ['a',1],
        ['b',2]
    ]
)

#prosto o[isaniye vnutrennego predstavleniya: levels
i4 = pd.MultiIndex(
    levels = [
        ['a','b','c'],
        [1,2]
    ],
    codes = [
        [0,0,1,1,2,2],
        [0,1,0,1,0,1]
    ]
)
#urovnyami mozhno zadavat nazvaniya

data = {
    ('city_1',2010):100,
    ('city_1',2020):200,
    ('city_2',2010):1001,
    ('city_2',2020):2001,
}
s = pd.Series(data)
print(s)

s.index_names = ['city','year']
print(s)

index = pd.MultiIndex.from_product(
    [
        ['city_1','city_2'],
        [2010,2020]
    ],
    names = ['city','year']
)

columns = pd.MultiIndex.from_product(
    [
        ['person_1','person_2','person_3'],
        ['job_1','job_2']
    ],
    names = ['worker','job']
)

rng = np.random.default_rng(1)

data = rng.random((4,6))
print(data)

data_df = pd.DataFrame(data,index=index,columns = columns)
print(data_df)

#indexatsia i srezi po multiindexu

data = {
    ('city_1',2010):100,
    ('city_1',2020):200,
    ('city_2',2010):1001,
    ('city_2',2020):2001,
}
s = pd.Series(data)
s.index_names = ['city','year']
print(s)
print(s['city_1',2010])
print(s['city_1'])
print(s.loc['city_1':'city_2'])

print(s[s>2000])
print(s[['city_1','city_3']])

#vzyat za osnovy dataframe s sled structuroi

#peregruppirovka multiindexov
rng = np.random.default_rng(1)
index = pd.MultiIndex.from_product(
    [
        ['a','c','b'],
        [1,2]
    ]
)

data = pd.Series(rng.random(6),index = index)
data.index.names = ['char','int']

print(data)
print(data['a':'b'])

data = data.sort_index()
print(data)
print(data['a':'b'])

index = [
    ('city_1',2010,1),
    ('city_1',2010,2),
    ('city_1',2020,1),
    ('city_1',2020,2),
    ('city_2',2010,1),
    ('city_2', 2010,2),
    ('city_2',2020,1),
    ('city_2', 2020,2),
    ('city_3',2010,1),
    ('city_3', 2010,2),
    ('city_3',2020,1),
    ('city_3',2020,2)
]

population = [
    101,
    1010,
    201,
    2010,
    102,
    1020,
    202,
    2020,
    103,
    1030,
    203,
    2030
]

pop = pd.Series(population,index=index)

print(pop)

i = pd.MultiIndex.from_tuples(index)

pop = pop.reindex(i)

print(pop)
print(pop.unstack(level=0))
print(pop.unstack(level=1))

#numpy concatenation

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

print(np.concatenate(x,y,z))
print(np.concatenate(x,y,z,axis =1))
print(np.concatenate(x,y,z,axis = 0))

ser1 = pd.Series(['a','b','c'],index = [1,2,3])
ser2 = pd.Series(['d','e','f'],index = [4,5,6])

print(pd.concat([ser1,ser2],verify_integrity=False))
print(pd.concat([ser1,ser2],ignore_index=True))
print(pd.concat([ser1,ser2],keys=['x','y']))

print(pd.concat([ser1,ser2],join = 'outer'))
print(pd.concat([ser1,ser2],join = 'inner'))

