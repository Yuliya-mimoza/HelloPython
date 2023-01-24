# 1.=====
# Cоздайте список из случайных чисел.
# Найдите номер его последнего локального максимума
# (локальный максимум — это элемент, который больше любого из своих соседей).
# import random
# n = int(input("Сколько элементов? "))
# list1 = []
# for i in range(n):
#     list1.append(random.randint(1, 10))
# print('Cделан такой список -', list1)

# for i in range(1,len(list1)-1):
#     if list1[i-1] < list1[i] > list1[i + 1]:
#         temp = i
# print(temp)


# 2.=====
# # Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
# import random
# n = int(input("Сколько элементов? "))
# list = []
# for i in range(n):
#     list.append(random.randint(1, 10))
# print('Cделан такой список -', list)
# max_count=0
# for i in range(len(list)):
#     if list.count(list[i])>max_count:
#        max_count=list.count(list[i])
# print(max_count)


# 3.=====
# Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2
# import random
# n = int(input("Сколько элементов? "))
# list = []
# for i in range(n):
#     list.append(random.randint(1, 100))
# print('Cделан такой список -', list)
# max1 = max(list)
# max2 = 0
# for i in range(len(list)):
#     if max1 > list[i] > max2:
#         max2 = list[i]
# print("Первый максимум = ", max1, "второй максимум = ", max2)


# # 4.=====
# # Создайте список из случайных чисел. Найдите количество различных элементов в нем.
# import random
# n = int(input("Сколько элементов? "))
# list = []
# for i in range(n):
#     list.append(random.randint(1, 10))
# print('Cделан такой список -', list)
# count = len(set(list))
# print('Количество различных элементов = ', count)




# # 5.=====
# # Пользователь вводит имя, фамилия, возраст. Создайте словарь user и запишите данные пользователя в него.
# firstname = input('Enter your firstname: ')
# lastname = input('Enter your lastname: ')
# age = input('Enter your age: ')

# user = dict(firstname=firstname, lastname=lastname, age=age)
# print(user)



# # 6.=====
# # Выведите самое часто встречающееся слово в введенной строке.
# list_of_words = ['hello', 'hello', 'hi']
# words = {}

# for word in list_of_words:
#     words[word] = words.get(word, 0) + 1

# # Функция max может получать функцию в качестве второго аргумента
# freq_word = max(words, key=words.get)
# print(freq_word)