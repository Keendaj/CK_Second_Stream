import pandas as pd
import numpy as np

##Задание 1
print("Задание 1 \n\n")
index = [
    ('city_1', 2010),
    ('city_1', 2020),
    ('city_2', 2010),
    ('city_2', 2020),
    ('city_3', 2010),
    ('city_3', 2020),
]

population = [
    101,
    201,
    102,
    202,
    103,
    203,
]
pop = pd.Series(population, index = index)
pop_df = pd.DataFrame(
    {
        'total': pop,
        'something': [
            10,
            11,
            12,
            13,
            14,
            15,
        ]
    }
)

new_ind = pd.MultiIndex.from_tuples(index)
pop_df = pop_df.reindex(new_ind)
print(pop_df)
print('\n\n')

pop_df_1 = pop_df.loc['city_1', 'something']
print(pop_df_1)

print('\n\n')


pop_df_1 = pop_df.loc[['city_1', 'city_3'], ['total', 'something']]
print(pop_df_1)

print('\n\n')


pop_df_1 = pop_df.loc[['city_1', 'city_3'], 'something']
print(pop_df_1)


##Задание 2
print("Задание 2 \n\n")
index = pd.MultiIndex.from_product(
    [
        ["city_1", "city_2"],
        ["2010", "2020"]
    ],
    names=["city", "year"]
)

columns = pd.MultiIndex.from_product(
    [
        ["person_1", "person_2", "person_3"],
        ["job_1", "job_2"]
    ],
    names=["worker", "job"]
)

rng = np.random.default_rng(21)
data = rng.random(size=(4,6))

df = pd.DataFrame(data, index=index, columns=columns)

print(df)

print('\n\n')
data_2020 = df.xs("2020", level='year')
print(data_2020)
print('\n\n')
job_1_data = df.xs('job_1', level='job', axis=1)
print(job_1_data)
print('\n\n')

city1_job2_data = df.loc['city_1', pd.IndexSlice[:, 'job_2']]
print(city1_job2_data)

print('\n\n')

##Задание 3
print("Задание 3 \n\n")
idx = pd.IndexSlice

person_1_3_data = df.loc[:, idx[['person_1', 'person_3'], :]]

rng = np.random.default_rng(21)
data = rng.random(size=(4,6))

df = pd.DataFrame(data, index=index, columns=columns)

print(df)
print('\n\n')
print(person_1_3_data)

print('\n\n')

city_person_data = df.loc[idx['city_1', :], idx['person_1':'person_2', :]]

print(city_person_data)

print('\n\n')   

##Задание 4
print("Задание 4 \n\n")

s1 = pd.Series({'a': 1, 'b': 2, 'c': 3}, name='s1')

s2 = pd.Series({'b': 4, 'c': 5, 'd': 6}, name='s2')

print(s1)
print('\n\n')   
print(s2)
print('\n\n')   
inner_join = pd.concat([s1, s2], axis=1, join='inner')

print(inner_join)
print('\n\n')   
outer_join = pd.concat([s1, s2], axis=1, join='outer')

print(outer_join)
