# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
n = int(input("Введите количество чисел в списке: "))
some_list = []
for i in range(n):
    x = int(input())
    some_list.append(x)
print("Список: ", some_list)
new_list=[]
[new_list.append(i) for i in some_list if i not in new_list]
print("Новый список: ", new_list)