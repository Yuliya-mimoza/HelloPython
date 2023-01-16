# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Входные и выходные данные хранятся в отдельных текстовых файлах.
with open('c:/Users/Hp/Desktop/ГикБ/GIT/GIT for study/Python/HelloPython/HomeWork/HomeWork5/file38.txt', 'r', encoding='utf-8') as file:
    some_list = file.read().split()
    print(some_list)
rez_list=[i for i in some_list if 'абв' not in i]
print(rez_list)