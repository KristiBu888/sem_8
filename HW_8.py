# Дополнить справочник возможностью копирования данных из одного файла в другой.
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.


def read_file():
    file_name = 'phonebook1.txt'
    new_file = 'phonebook2.txt'
    try:
        with open(file_name, 'r', encoding='utf-8') as fd:
            data = fd.readlines()
            for idx, val in enumerate(data):
                print(f'{idx}) {val.rstrip()}')
            ind_str = input('Введите необходимый индекс: ')
            try:
                ind = int(ind_str)
                try:
                    print(f'{data[ind]}\n')
                    with open(new_file, 'a', encoding='utf-8') as f:
                        f.write(f'{data[ind]}\n')
                except IndexError:
                    print('Вы ввели несуществующий индекс')
            except ValueError:
                print('Надо ввести целое число')
    except FileNotFoundError as err:
        print('Файл еще не создан, введите данные', err)


read_file()
