import pytest

documents = [{
    "type": "passport",
    "number": "2207 876234",
    "name": "Василий Гупкин"
}, {
    "type": "invoice",
    "number": "11-2",
    "name": "Геннадий Покемонов"
}, {
    "type": "insurance",
    "number": "10006",
    "name": "Аристарх Павлов"
}]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_all_doc_owners_names():
    """
    Имена всех владельцев документов
    """
    users_list = []
    for current_document in documents:
        try:
            doc_owner_name = current_document['name']
            users_list.append(doc_owner_name)
        except KeyError:
            pass
    return set(users_list)


def get_doc_owner_name(number_document):
    """
    Имя владельца документа по номеру документа
    """
    # number_document = input('Введите номер документа - ')
    for document in documents:
        if number_document in document[
                'number'] and number_document == document['number']:
            return document['name']
    else:
        print('Документ с данным номером не найден!')
        return


def show_all_docs_info(documents):
    """
    Список всех документов
    """
    print('Список всех документов:\n')
    for document in documents:
        doc_type = document['type']
        doc_number = document['number']
        doc_owner_name = document['name']
        print(f'{doc_type} "{doc_number}" "{doc_owner_name}"')


def get_doc_shelf(number_document):
    """
    Номер полки по номеру документа
    """
    # number_document = input('Введите номер документа - ')
    for directory_key, directory_value in directories.items():
        if number_document in directory_value:
            return directory_key
    else:
        print('Документ с данным номером не найден!')
        return


def add_new_doc(number_document, type, name, shelf):
    """
    Добавление нового документа
    """
    # number_document = input('Введите номер документа - ')
    # type = input('Введите тип документа - ')
    # name = input('Введите имя владельца документа- ')
    # shelf = input('Введите номер полки для хранения - ')
    documents.append({"type": type, "number": number_document, "name": name})
    directories[shelf] = []
    directories[shelf].append(number_document)
    return number_document, shelf


def delete_document(number_document):
    """
    Удаление документа
    """
    # number_document = input('Введите номер документа: ')
    for document in documents:
        if number_document in document['number']:
            documents.remove(document)
            for directories_values in directories.values():
                if number_document in directories_values:
                    directories_values.remove(number_document)
                    return number_document
    else:
        print('Документ с данным номером не найден!')
        return


def move_doc_to_shelf(number_document, number_shelf):
    """
    Перемещение документа с одной полки на другую
    """
    # number_document = input('Введите номер документа - ')
    # number_shelf = input('Введите номер полки для перемещения - ')
    if number_shelf not in directories:
        directories[number_shelf] = []
    for directories_key, directories_value in directories.items():
        if number_document in directories_value:
            directories[number_shelf] += [number_document]
            directories_value.remove(number_document)
            return number_document, number_shelf
    print(f'Документа с номером {number_document} не существует')


def add_shelf(number_shelf):
    """
    Добавление полки
    """
    # number_shelf = input('Введите номер полки - ')
    if number_shelf not in directories:
        directories[number_shelf] = []
        return number_shelf
    else:
        print(
            f'Такая полка уже существует. Текущий перечень полок: {", ".join(directories.keys())}'
        )
        return


def secretary_program_start():
    """
    ap - (all people) - команда, которая выводит список всех владельцев документов
    p – (people) – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
    l – (list) – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
    s – (shelf) – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
    a – (add) – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип,
    имя владельца и номер полки, на котором он будет храниться.
    d – (delete) – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
    m – (move) – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
    as – (add shelf) – команда, которая спросит номер новой полки и добавит ее в перечень;
    q - (quit) - команда, которая завершает выполнение программы
    """
    print('Вас приветствует программа помошник!\n',
          '(Введите help, для просмотра списка поддерживаемых команд)\n')
    while True:
        user_command = input('Введите команду - ')

        if user_command == 'p':
            owner_name = get_doc_owner_name(
                number_document=input('Введите номер документа - '))
            if owner_name:
                print(f'Владелец документа - {owner_name}')

        elif user_command == 'ap':
            uniq_users = get_all_doc_owners_names()
            print(f'Список владельцев документов - {uniq_users}')

        elif user_command == 'l':
            show_all_docs_info(documents)

        elif user_command == 's':
            directory_number = get_doc_shelf(
                number_document=input('Введите номер документа - '))
            if directory_number:
                print(f'Документ находится на полке номер {directory_number}')

        elif user_command == 'a':
            print('Добавление нового документа:')
            new_doc_ = add_new_doc(
                number_document=input('Введите номер документа - '),
                type=input('Введите тип документа - '),
                name=input('Введите имя владельца документа- '),
                shelf=input('Введите номер полки для хранения - '))
            print(
                f'\nНа полку "{new_doc_[1]}" добавлен новый документ номер: "{new_doc_[0]}"'
            )

        elif user_command == 'd':
            doc_number = delete_document(
                number_document=input('Введите номер документа: '))
            if doc_number:
                print(f'Документ с номером "{doc_number}" был успешно удален')

        elif user_command == 'm':
            new_shelf = move_doc_to_shelf(
                number_document=input('Введите номер документа - '),
                number_shelf=input('Введите номер полки для перемещения - '))
            if new_shelf:
                print(
                    f'Документ с номером {new_shelf[0]} перемещен на полку номер {new_shelf[1]}'
                )

        elif user_command == 'as':
            shelf_number = add_shelf(
                number_shelf=input('Введите номер полки - '))
            if shelf_number:
                print(
                    f'Полка  с номером "{shelf_number}" добавлена. Текущий перечень полок: {", ".join(directories.keys())}'
                )

        elif user_command == 'help':
            print(secretary_program_start.__doc__)

        elif user_command == 'q':
            break

