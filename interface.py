
database = {}
db = {'parents': 1, 'children': 2}


def reading_file_to_dict(number_file):
    with open(f'{number_file}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[number_file] = []
    for i in data:
        database[number_file].append(tuple(i.split(';')))
    print(database)


def print_childrens(second_name):
    with open(f'{1}.txt', 'r', encoding='utf-8') as file_1:
        data = [i.split('\n')[0] for i in file_1.readlines()]
        database[1] = []
    for i in data:
        database[1].append(tuple(i.split(';')))
    with open(f'{2}.txt', 'r', encoding='utf-8') as file_2:
        data = [i.split('\n')[0] for i in file_2.readlines()]
        database[2] = []
    for i in data:
        database[2].append(tuple(i.split(';')))
    id = [i[0] for i in database[db['parents']]if second_name in i][0]
    deti = [i for i in database[db['children']] if id == i[1]]
    print(*[' '.join(i[2:4])+'\n' for i in deti])


def new_str():
    with open(f'{1}.txt', 'a', encoding='utf-8') as file_3:
        id = input('Введите уникальный номер:\n')
        name = input('Введите имя:\n')
        second_name = input('Введите фамилию:\n')
        file_3.write(f'{id};{name};{second_name}\n')
        having_children = int(input('Есть ли дети?\n1.Есть\n2.Нет\n'))
        while having_children != 1 and having_children != 2:
          print('Введите корректный номер')
          having_children = int(input("Выбирите номер: "))
        if having_children == 1:
            with open(f'{2}.txt', 'a', encoding='utf-8') as file_4:
                id_children = int(input('Введите уникальный номер ребенка:\n'))
                name_children = input('Введите имя ребенка:\n')
                bd_children = input(
                    'Введите дату рождения ребенка в формате 01.01.2000\n')
                file_4.write(
                    f'{id_children};{id};{name_children};{second_name};{bd_children}\n')
        else:
            pass
        print('Запись успешно сохранена')


def menu():
    question = int(input('Выбирите номер:\n'
                         '1.Посмотреть базу\n'
                         '2.Новая запись\n'
                         '3.Поиск детей\n'))
    while question != 1 and question != 2 and question != 3:
        print('Введите корректный номер')
        question = int(input("Выбирите номер: "))
    if question == 1:
        question_2 = int(input('1.Сотрудники\n'
                               '2.Дети сотрудников\n'))
        while question_2 != 1 and question_2 != 2:
          print('Введите корректный номер')
          question_2 = int(input("Выбирите номер: "))
        reading_file_to_dict(question_2)
    elif question == 2:
        new_str()
    elif question == 3:
        print_childrens(input('Введите фамилию:\n'))
