def write_name():
    name = input('Введите имя: ')
    return name

def write_surname():
    surname = input('Введите фамилию: ')
    return surname

def write_phone():
    phone = input('Введите телефон: ')
    return phone

def write_adress():
    adress = input('Введите адрес: ')
    return adress

def input_data(a=None):
    name = write_name()
    surname = write_surname()
    phone = write_phone()
    adress = write_adress()
    with open('phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(f'{name} {surname}: {phone}\n{adress}\n\n')


def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        data_first = data.readlines()
        for line in data_first:
            print(line, end='')


def search_line():
    search = input('Введите данные для поиска: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        for line in data_first:
            if search in line:
                print(line)

"""Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных."""


def interface():
    command = 0
    while command != '6':
        print('''Что вы хотите сделать?
         1 - запись данных
         2 - вывод данных
         3 - поиск данных
         4 - удаление данных
         5 - замена конктакта на новый
         6 - выход''')
        command = input('Введите номер операции: ')
        while command not in ('1', '2', '3', '4', '5', '6'):
            print('Введите корректную команду!')
            command = input('Введите номер операции: ')

        if command == '1':
            input_data()
        elif command == '2':
            print_data()
        elif command == '3':
            search_line()
        elif command == '4':
            delete_data()
        elif command == '5':
            replacement ()
                

def delete_data():
    search = input('Введите данные для удаления: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        data_first = data_first[:-1]
        with open('phonebook.txt', 'w', encoding='utf-8')as data:
            for line in data_first:
                if search not in line:
                    data.write(f'{line}\n\n')

def replacement ():
    search = input('Введите данные для замены: ')
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        temp = data.readlines()
        data_first = ''.join(temp).split('\n\n')
        data_first = data_first[:-1]
        with open('phonebook.txt', 'w+', encoding='utf-8')as data:
            for line in data_first:
                if search in line:
                    name = write_name()
                    surname = write_surname()
                    phone = write_phone()
                    adress = write_adress()
                    data.write(f'{name} {surname}: {phone}\n{adress}\n\n')
                else:
                    data.write(f'{line}\n\n')

interface()