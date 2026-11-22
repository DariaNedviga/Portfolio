from tabulate import tabulate
from database import database


def get_integer(text: str) -> int or None:
    try:
        command = int(input(f'{text} '))
    except:
        command = None
        print('Вы ввели не число')
    return command


def program():
    while True:
        db = database('ddd.db')
        print('Программа банка "Триумф"')
        print('1. Таблица клиент')
        print('2. Таблица вклад')
        print('3. Таблица кредит')
        print('4. Таблица банковские карты')
        print('5. Таблица менеджеры')
        print('6. Таблица отделения банка')
        print('7. Таблица паспортные данные')
        print('8. Связать банковскую карту и клиента')
        print('9. Выход из программы')
        command = get_integer('> ')
        match command:
            case 1:
                print('|Клиенты|')
                print('1. Добавление клиента')
                print('2. Список клиентов')
                print('3. Удаление клиента')
                print('4. Изменение данных о клиенте')
                print('9. Выход из программы')
                command = get_integer('> ')
                match command:
                    case 1:
                        print('|добавление клиента|')
                        manager = input('Введите фамилию менеджера: ')
                        name = input('Введите имя: ')
                        surname = input('Введите фамилию: ')
                        patronymic = input('Введите отчество: ')
                        age = int(input('Введите возраст: '))
                        phone_number = int(input('Введите номер телефона: '))
                        bank = input('Введите название банка: ')
                        request = f'INSERT INTO client VALUES (NULL, (SELECT id FROM manager WHERE last_name = "{manager}"), "{name}", "{surname}", "{patronymic}", "{age}", "{phone_number}", (SELECT id FROM bank WHERE name = "{bank}"));'
                        response = db.raw(request)
                        if response:
                            print('Клиент добавлен в БД')
                        else:
                            print('Клиент НЕ добавлен в БД, проверьте вводимые значения')
                    case 2:
                        print('|Вывод клиентов|')
                        order = input('Введите тип сортировки: (ASC/DESC): ')
                        request = (f'SELECT client.last_name, client.first_name, client.phone_number,'
                                   f' bank.name AS bank_name, manager.last_name AS manager FROM client'
                                   f' JOIN bank on bank.id  = client.bank_id  JOIN manager ON manager.id'
                                   f' = client.manager_id ORDER BY client.last_name {order};')
                        response = db.raw(request)
                        for row in response:
                            print(f' {row["last_name"]}\t{row["first_name"]}\t{row["phone_number"]}\t{row["bank_name"]}'
                                  f'\t{row["manager"]}')
                    case 3:
                        print('|Удаление клиента|')
                        name = input('Введите имя клиента')
                        surname = input('Введите фамилию клиента')
                        request = (f' DELETE FROM client WHERE id ='
                                   f' (SELECT id FROM client WHERE first_name = "{name}" AND last_name = "{surname}");')
                        response = db.raw(request)
                        print("Клиент удален")
                    case 4:
                        id = get_integer('id студента: ')
                        if id is not None:
                            print('|Изменение данных о клиенте|')
                            print('1. Изменение фамилии')
                            print('2. Изменение имени')
                            print('3. Изменение группы')
                            print('9. Назад')
                            command = get_integer('> ')
                            match command:
                                case 1:
                                    request = f'SELECT last_name FROM client WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]['last_name']
                                    surname = input("Введите фамилию")
                                    request = f'UPDATE client SET last_name == "{surname}" WHERE id == {id};'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили фамилию у клиента {id} с {y} на {surname}')
                                    else:
                                        print('Фамилия у клиента НЕ изменена, проверьте вводимые значения')
                                case 2:
                                    request = f'SELECT first_name FROM client WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]['first_name']
                                    name = input("Введите имя")
                                    request = f'UPDATE client SET first_name == "{name}" WHERE id == {id};'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили имя у клиента {id} с {y} на {name}')
                                    else:
                                        print('Имя у клиента НЕ изменено, проверьте вводимые значения')
                                case 3:
                                    request = f' SELECT age FROM client WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]['age']
                                    age = int(input("Введите возраст"))
                                    request = f' UPDATE client SET age == "{age}" WHERE id == {id};'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили возраст у клиента {id} с {y} на {age}')
                                    else:
                                        print('Возраст у клиента НЕ изменен, проверьте вводимые значения')
            case 2:
                print('|Вклад|')
                print('1. Добавление вклада')
                print('2. Список вкладов')
                print('3. Удаление вклада')
                print('4. Изменение данных о вкладе')
                print('9. Выход из программы')
                command = get_integer('> ')
                match command:
                    case 1:
                        print('|добавление вклада|')
                        client_name = (input("Введите имя клиента"))
                        client_surname = (input("Введите фамилию клиента"))
                        client_phone = int(input("Введите номер телефона клиента"))
                        name = input("Введите название вклада")
                        interest = float(input("Введите процент по вкладу"))
                        cash_out = bool(input("Введите возможность вывода true/false"))
                        maturity = input("Введите срок вклада")
                        request = f'INSERT INTO investment VALUES(NULL, (SELECT id FROM client WHERE last_name = "{client_surname}" AND first_name = "{client_name}" AND phone_number = "{client_phone}"),"{name}", {interest}, {cash_out}, {maturity});'
                        response = db.raw(request)
                        if response:
                            print('Вклад добавлен в БД')
                        else:
                            print('Вклад НЕ добавлен в БД, проверьте вводимые значения')
                    case 2:
                        print('|Вывод клиентов|')
                        limit = input('Введите органичения для offset_limit : (2,5): ')
                        request = (f' SELECT investment.id, investment.name, investment.interest_rate, investment.cash_out_possibility,'
                                   f' investment.maturity, client.first_name AS client_name, client.last_name AS client_surname'
                                   f' FROM investment JOIN client ON client.id = investment.client_id LIMIT {limit};')
                        response = db.raw(request)
                        print(tabulate(response, headers=['id', 'name', 'interest_rate', 'cash_out_possibility', 'maturity', 'client_name', 'client_surname']))
                    case 3:
                        print('|Удаление вклада|')
                        id = get_integer('id вклада: ')
                        if id is not None:
                            request = f'DELETE FROM investment WHERE id == {id};'
                            response = db.raw(request)
                            print('вклад удален')
                    case 4:
                        print('|Изменение данных о вкладе|')
                        id = get_integer('id вклада: ')
                        if id is not None:
                            print('|Изменение данных о вкладе|')
                            print('1. Изменение названия')
                            print('2. Изменение процента')
                            print('3. Изменение возможности снятия')
                            print('4. Изменение срока')
                            print('5. Изменение id клиента')
                            print('9. Назад')
                            command = get_integer('> ')
                            match command:
                                case 1:
                                    request = f'SELECT name FROM investment WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]['name']
                                    name = input("Введите название")
                                    request = f' UPDATE investment SET name == "{name}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили название у вклада {id} с {y} на {name}')
                                    else:
                                        print('Название у вклада НЕ изменено, проверьте вводимые значения')
                                case 2:
                                    request = f' SELECT interest_rate FROM investment WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]('interest_rate')
                                    rate = float(input("Введите процент по вкладу"))
                                    request = f' UPDATE investment SET interest_rate == "{rate}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили процент у вклада {id} с {y} на {rate}')
                                    else:
                                        print('Процент у вклада НЕ изменен, проверьте вводимые значения')
                                case 3:
                                    request = f' SELECT cash_out_possibility FROM investment WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]('cash_out_possibility')
                                    cash = bool(input("Введите возможность снятия true/false"))
                                    request = f' UPDATE investment SET cash_out_possibility == "{cash}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили возможность снятия у вклада {id} с {y} на {cash}')
                                    else:
                                        print('Возможность снятия у вклада НЕ изменена, проверьте вводимые значения')
                                case 4:
                                    request = f' SELECT maturity FROM investment WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]('maturity')
                                    maturity = int(input("Введите срок вклада"))
                                    request = f' UPDATE investment SET maturity == "{maturity}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили срок у вклада {id} с {y} на {cash}')
                                    else:
                                        print('Срок у вклада НЕ изменен, проверьте вводимые значения')
                                case 5:
                                    client_id = int(input("Введите id клиента"))
                                    request = f' UPDATE investment SET client_id == "{client_id}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили id клиента у вклада {id} с {y} на {cash}')
                                    else:
                                        print('ID клиента у вклада НЕ изменен, проверьте вводимые значения')
            case 4:
                print('|Банковская карта|')
                print('1. Добавление банковской карты')
                print('2. Список банковских карт')
                print('3. Удаление банковской карты')
                print('4. Изменение данных о банковской карте')
                print('9. Выход из программы')
                command = get_integer('> ')
                match command:
                    case 1:
                        print('|добавление банковской карты|')
                        type = input("Введите тип банковской карты")
                        price = int(input("Введите стоимость обслуживания"))
                        limit = int(input("Введите лимит для снятия"))
                        acc = float(input("Введите процент накопления"))
                        contact = bool(input("Введите возможность бесконтактной оплаты true/false"))
                        mile = bool(input("Введите возможность накопления миль true/false"))
                        swift = bool(input("Введите наличие подключения к swift true/false"))
                        request = f' INSERT INTO bank_card VALUES (NULL, "{type}", "{price}", "{limit}", "{acc}", "{contact}", "{mile}", "{swift}");'
                        response = db.raw(request)
                        if response:
                            print('Банковская карта добавлена в БД')
                        else:
                            print('Банковская карта НЕ добавлена в БД, проверьте вводимые значения')
                    case 2:
                        print('|Вывод банковских карт|')
                        between_1 = int(input("Введите нижнюю границу для лимита по снятию"))
                        between_2 = int(input("Введите верхнюю границу для лимита по снятию"))
                        request = (f' SELECT bank_card.id, bank_card.type, bank_card.service_price, bank_card.cash_out_limit,'
                                   f' bank_card.accumulation_by_balance, bank_card.contactless_payments, bank_card.miles_accumulation, bank_card.swift,'
                                   f' client.last_name AS client_surname, client.first_name AS client_name FROM card_client'
                                   f' JOIN bank_card ON card_client.card_id = bank_card.id JOIN client ON card_client.client_id = client.id WHERE cash_out_limit'
                                   f' BETWEEN {between_1} AND {between_2};')
                        response = db.raw(request)
                        print(tabulate(response, headers = ['id', 'type', 'service_price', 'limit', 'accumulation_by_balance', 'contactless_payments', 'miles_accumulation', 'swift', 'client_surname', 'client_name']))
                    case 3:
                        print('|Удаление банковской карты|')
                        id = get_integer('id банковской карты: ')
                        if id is not None:
                            request = f'DELETE FROM bank_card WHERE id == {id};'
                            response = db.raw(request)
                            print('банковская карта удалена')
                    case 4:
                        print('|Изменение данных о банковской карте|')
                        id = get_integer('id вклада: ')
                        if id is not None:
                            print('|Изменение данных о банковской карте|')
                            print('1. Изменение типа')
                            print('2. Изменение стоимости обслуживания')
                            print('3. Изменение лимита на снятие')
                            print('4. Изменение накопления по остатку')
                            print('5. Изменение возможности бесконтактных платежей')
                            print('6. Изменение возможности накопления миль')
                            print('7. Изменение подключения к swift')
                            print('8. Изменение id клиента')
                            print('9. Назад')
                            command = get_integer('> ')
                            match command:
                                case 1:
                                    request = f'SELECT type FROM bank_card WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]('type')
                                    type = input("Введите тип")
                                    request = f' UPDATE bank_card SET type == "{type}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили тип у банковской карты {id} с {y} на {type}')
                                    else:
                                        print('Тип у банковской карты НЕ изменен, проверьте вводимые значения')
                                case 2:
                                    request = f' SELECT service_price FROM bank_card WHERE id == {id};'
                                    x =db.raw(request)
                                    y = x[0]('service_price')
                                    price = int(input("Введите стоимость обслуживания"))
                                    request = f' UPDATE bank_card SET service_price == "{price}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(f'Вы успешно изменили стоимость обслуживания у банковской карты {id} с {y} на {type}')
                                    else:
                                        print('Стоимость обслуживания у банковской карты НЕ изменена, проверьте вводимые значения')
                                case 3:
                                    request = f' SELECT cash_out_limit FROM bank_card WHERE id == {id};'
                                    x = db.raw(request)
                                    y = x[0]('cash_out_limit')
                                    limit = int(input("Введите лимит на снятие"))
                                    request = f' UPDATE bank_card SET cash_out_limit == "{limit}" WHERE id == "{id}";'
                                    response = db.raw(request)
                                    if response:
                                        print(
                                            f'Вы успешно изменили лимит на снятие у банковской карты {id} с {y} на {limit}')
                                    else:
                                        print(
                                            'Лимит на снятие у банковской карты НЕ изменен, проверьте вводимые значения')
                                case 4:
                                    request = f' SELECT accumulation_by_balance FROM bank_card WHERE id == {id};'
                                    x = db.raw(request)
                                    
            case 9:
                break
if __name__ == '__main__':
    program()
