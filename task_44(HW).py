"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит 
всего из 1 столбца. Ваша задача перевести его в one hot вид. Сделать без 
без встроенных функций!

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

"""

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})

unique_values = {val: i for i, val in enumerate(set(lst))}
one_hot_encoded = []
for item in lst:
    one_hot_vector = [0] * len(unique_values)
    index = unique_values[item]
    one_hot_vector[index] = 1
    one_hot_encoded.append(one_hot_vector)

one_hot_df = pd.DataFrame(one_hot_encoded, columns=unique_values.keys())

print(f'{data.head()}\n\n')
print(one_hot_df.head())
