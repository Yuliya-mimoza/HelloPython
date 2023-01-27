# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
path = "c:/Users/Hp/Desktop/ГикБ/GIT/GIT for study/Python/HelloPython/HomeWork/HomeWork5/HomeWork5_1Input.txt"
with open (path, 'r', encoding='utf-8') as file:
    text = file.readline()

new_text = ''
i = 0
while i < len(text):
    simbol = text[i]
    count = 0
    for j in range(i + 1, len(text)):
        if simbol == text[j]:
            if text[j] == text[j - 1]:
                count += 1
        else:
            break
    new_text += str(count + 1) + simbol
    i = i + count + 1

fig = 0
for item in new_text:
    if item.isdigit():
        fig += 1

text = ''
i = 0
while i < len(new_text):
    if new_text[i].isdigit() and not new_text[i + 1].isdigit():
        text += new_text[i + 1] * int(new_text[i])
        i += 2
    else:
        flag = 2
        for j in range(i + 2, i + fig):
            if new_text[j].isdigit():
                flag += 1
            else:
                flag1 = ''
                for k in range(i, i + flag):
                    flag1 += new_text[k]
                text += new_text[i + flag] * int(flag1)
                break
        i += flag + 1

with open ('c:/Users/Hp/Desktop/ГикБ/GIT/GIT for study/Python/HelloPython/HomeWork/HomeWork5/HomeWork5_1Output.txt', 'w', encoding='utf-8') as file:
    file.write(new_text + '\n' + text)