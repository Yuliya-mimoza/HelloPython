def inp_mod():
    mod = input('Введите режим работы ("импорт" или "экспорт"): ')
    return mod


def inp_import():
    surname = input('Введите фамилию для поиска: ')
    return surname


def inp_export():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    sec_name= input('Введите отчество: ')
    phone = input('Введите телефон: ')
    comment = input('Введите тип телефона (домашний, рабочий): ')
    return '\n',surname,name, sec_name,phone, comment


def view_import(result):
    print(*result, sep='\n')


def view_import_no():
    print(f'Данные не найдены')


def view_export():
    print(f'Введенные данные успешно сохранены')