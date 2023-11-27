import HW_8


def show_all(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.readlines()
        print("".join(data))


def add_new(file_name: str):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона без пробелов: ')
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')


def main():
    file_name = 'phonebook2.txt'
    flag_exit = False
    while not flag_exit:
        print('1 - показать все записи')
        print('2 - добавить все запись')
        answer = input('Введите операцию или x для выхода: ')
        if answer == '1':
            show_all(file_name=file_name)
        elif answer == '2':
            add_new(file_name)
        elif answer == 'x':
            flag_exit = True


if __name__ == '__main__':
    main()
