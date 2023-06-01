# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его 
# кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе 
# стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух 
# вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке 
# и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def is_rhythm(count_vowels: list[int]) -> None:
    """Принимает на вход список, последовательно сравнивает элементы списка и выводит сообщение о наличии рифмы"""
    for i in range(len(count_vowels)):
        if count_vowels[0] != count_vowels[i] and len(count_vowels) > 1:
            return print('Пам парам')
        if len(count_vowels) == 1 and count_vowels[i] % 2 != 0:
            return print('Пам парам')
    return print('Парам пам-пам')

vowels = 'аеёиоуыэюя'
poem = input('Введите стих: ').lower().replace('-', '').split()
print(poem)
# count_vowels = []
# for phrase in poem:
#     count = 0
#     for char in phrase:
#         if char in vowels:
#             count += 1
#     count_vowels.append(count)
count_vowels = [sum(len(list(filter(lambda i: i in vowels, char))) for char in phrase) for phrase in poem]
print(count_vowels)
is_rhythm(count_vowels)