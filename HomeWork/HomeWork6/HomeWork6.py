# 1.=====
# Пользователь вводит число K - количество фруктов.
# Затем он вводит K фруктов в формате: название фрукта и его количество.
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение.
# dictFruit={}
# count = int(input("Введите количество фруктов: "))
# for i in range(count):
#         name = input("Введите название фрукта: ")
#         countFruit = int(input("Количество: "))
#         dictFruit[name] = countFruit
# print(dictFruit)


# 2.=====
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.
# friends = []
# n = int(input("Введите количество друзей: "))
# for i in range(n):
#     name = input("Введите имя друга: ")
#     age = int(input("Введите возраст друга: "))
#     friends.append(dict(name=name, age=age))
# print(friends)
# minage = min(friends, key=lambda x: x['age'])
# print('Младшего из друзей зовут: ', minage['name'])


# 3.=====
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.
# friends = []
# sumage = 0
# srednii = 0
# n = int(input("Введите количество друзей: "))
# for i in range(n):
#     name = input("Введите имя друга: ")
#     age = int(input("Введите возраст друга: "))
#     friends.append(dict(name=name, age=age))
#     sumage = sumage+age
# print(friends)
# srednii = sumage/n
# print('Средний возраст всех друзей = ', srednii, ' года')
# max_name = max(friends, key=lambda x: len(x['name']))
# print('Самое длинное имя =', max_name['name'])


# 4.=====
# "Пора учить английский язык", - сказал себе Степа и решил написать программу для изучения английского языка.
# Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
# Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().
# dict = {}
# n = int(input("Введите количество английских слов: "))
# for i in range(n):
#     english = input("Введите английское слово: ")
#     russian = input("Введите несколько его переводов на русском языке через пробел: ")
#     dict[english] = russian.split()
# print(dict)

# 4.=====вариант преподавателя
count = int(input())
translate_dict = {}
for _ in range(count):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
eng_word = input('Введите слово для перевода: ')
if translate_dict.get(eng_word):
    print(', '.join(translate_dict.get(eng_word)))
else:
    print('Такого слова нет')


# 5.=====
# Создайте список из случайных чисел. Найдите количество различных элементов в нем.
# import random
# n = int(input("Сколько элементов? "))
# list = []
# for i in range(n):
#     list.append(random.randint(1, 10))
# print('Cделан такой список -', list)
# count = len(set(list))
# print('Количество различных элементов = ', count)
