# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
n = int(input("Введите количество чисел в списке: "))
some_list = []
for i in range(n):
    x = float(input())
    some_list.append(x)
print("Список: ", some_list)
some_list2 = []
for i in range(n):
    x = some_list[i] % 1
    some_list2.append(round(x, 2))
print("Новый список из дробной части: ", some_list2)
raz = 0
for i in range(n):
    min = some_list2[0]
    max = some_list2[1]
    if some_list2[i] > max:
        max = some_list2[i]
    if some_list2[i] < min:
        min = some_list2[i]
raz = max-min
print("Max = ", max, "Min = ", min)
print("Разница между максимальным и минимальным значением дробной части элементов равна: ", round(raz, 2))
