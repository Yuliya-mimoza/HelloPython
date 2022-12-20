# """Задача 2""" с вариантами
# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

some_list = []
for _ in range(5):  # 0, 1, 2, 3, 4
    x = int(input())
    some_list.append(x)
maxx = some_list[0]
for el in some_list:
    if el > maxx:
        maxx = el
print(maxx)

# maxx = int(input())
# for _ in range(4):  # 0, 1, 2, 3
#     x = int(input())
#     if x > maxx:
#         maxx = x
# print(maxx)

# print(max(some_list))

# maxx = some_list[0]
# for el in some_list:  # 6, 7, 0, -1, 4
#     if el > maxx:
#         maxx = el
# print(maxx)

# maxx = some_list[0]
# for ind in range(5):
#     if some_list[ind] > maxx:
#         maxx = some_list[ind]
# print(maxx)
