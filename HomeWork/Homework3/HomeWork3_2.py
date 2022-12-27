# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
n = int(input("Введите количество чисел в списке: "))
some_list = []
for i in range(n):
    x = int(input())
    some_list.append(x)
print("Список: ", some_list)
some_list2 = []
if n % 2 == 0:
    for i in range(n//2):
        x = some_list[i]*some_list[n-1-i]
        some_list2.append(x)
if n % 2 != 0:
    for i in range(n//2):
        x = some_list[i]*some_list[n-1-i]
        some_list2.append(x)
    some_list2.append(some_list[n//2]**2)
print("Новый список: ", some_list2)
