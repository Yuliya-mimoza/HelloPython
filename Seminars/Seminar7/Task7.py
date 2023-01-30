# передаем в функцию неизвестное количество аргументов - "*"
# summa('alex',1,3,5,7,9,...)
def summa(name, *args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


summa('alex', 1, 3, 5, 7, 9)



# передаем в функцию неизвестное количество аргументов в словаре- "**"
def full_name(age, *kwargs):
    print(kwargs)


full_name(20, name='alex', surname='salnikov')


# передаем в функцию неизвестное количество аргументов в словаре- "**"
# если ничего не передаем, то напечатает - "Незнакомец", если передадим имя, то имя
def full_name(name='Незнакомец'):
    print(name)


full_name('alex')