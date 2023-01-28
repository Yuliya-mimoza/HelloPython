import datetime

def log(rezh, result):
    path='Python\HelloPython\HomeWork\HomeWork7\log.txt'
    with open(path, 'a', encoding='utf-8') as file:
        if rezh.lower()=='импорт':
            file.write(f'Поиск фамилии "{result}" в справочнике: {str(datetime.datetime.now())} \n')
        elif rezh.lower() == 'экспорт':
            file.write(f'Фамилия "{result}" добавлена в справочник: {str(datetime.datetime.now())} \n')