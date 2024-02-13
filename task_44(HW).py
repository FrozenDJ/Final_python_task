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