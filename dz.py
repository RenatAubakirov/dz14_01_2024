"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сделать без встроенных ф-ций, например,get_dummies?
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
data = pd.DataFrame({'whoAmI': lst})
data.head()

def one_hot(data, column_name):
    unique_values = data[column_name].unique()
    for value in unique_values:
       data[f'whoAmI_{value}'] = (data[column_name] == value).astype(int)

    data.drop(column_name, axis=1, inplace=True)

one_hot(data, 'whoAmI')
print(data)
