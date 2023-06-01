# Задача 36:
# На вход программы поступает строка в формате:
# ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N
# Необходимо с помощью функции map преобразовать ее в кортеж tp вида:
# tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
# Выводить на экран ничего не нужно, только преобразовать строку в кортеж с именем tp.

# Sample Input:

# house=дом car=машина men=человек tree=дерево
# Sample Output:
# (('house', 'дом'), ('car','машина'), ('men', 'человек'), ('tree', 'дерево'))
import re

string = 'house=дом car=машина men=человек tree=дерево'
list_of_string = re.split("=| ", string)
list_1 = [list_of_string[i] for i in range(len(list_of_string)) if i % 2 == 0]
list_2 = [list_of_string[i] for i in range(len(list_of_string)) if i % 2 != 0]
tp = tuple(map(tuple, zip(list_1, list_2)))
print(tp)