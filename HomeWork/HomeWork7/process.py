def search(sn):
    rez_list=[]
    path='Python\HelloPython\HomeWork\HomeWork7\data.txt'
    with open (path, 'r', encoding='utf-8') as file:
        while True:
            my_book=file.readline()
            if not my_book:
                if not file.readline():
                    break
            if my_book.rstrip()==sn:
                rez_list.append(sn)
                for i in range(1,5):
                    rez_list.append(file.readline().rstrip())
                rez_list.append('')
    if len(rez_list)>0:
        return rez_list
    return 'Таких людей не найдено'


def export(res):
    path='Python\HelloPython\HomeWork\HomeWork7\data.txt'
    with open (path, 'a', encoding='utf-8') as file:
        for ind in range(5):
            file.write(res[ind]+'\n')
        file.write(res[5])
