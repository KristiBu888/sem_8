# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

def show_all(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))


def copy(file_name: str, option: bool):
    old_data = find_by_attribute(file_name, True)
    print("Введите id нужного пользователя для копирования данных:\n")
    data = ""
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        i = data.index(old_data)
        if option:
            id = input("Введите id нужного пользователя для изменения данных: ")
        else:
            id = input("Введите id нужного пользователя: ")
        return data[int(id)-1]
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(data)


def find_by_attribute(file_name: str, option: bool):
    c = input("Введите 1 для поиска по фамилии, 2 для поиска по имени")
    opt = 0
    if c == '1':
        opt = 0
    elif c == '2':
        opt = 1
    attr = input("Введите имя/фамилию для поиска")
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        data = list(filter(lambda x: x.split(', ')[opt] == attr, data))
        print(list(zip(range(1, len(data)+1), data)))
    if option:
        id = input("Введите id нужного пользователя для изменения данных: ")
    else:
        id = input("Введите id нужного пользователя: ")
    return data[int(id)-1]


def add_new(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона без пробелов: ')
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')


def main():
    file_name = 'phonebook1.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить все запись')
        print('4 - копировать запись')
        print('5 - поиск записи по имени/фамилии')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == '4':
            copy(file_name=file_name)
        elif answer == '5':
            print(find_by_attribute(file_name, False))
        elif answer == 'x':
            flag_exit = True


if __name__ == '__main__':
    main()
