from classes import Record, AddressBook


phone_book = AddressBook()


# Декоратор ошибок
def input_error(func):
    def inner_func(text):
        try:
            return func(text)
        except IndexError:
            return "Please enter command, name and phone number"
        except KeyError:
            return "No such name in the phone book"
        except ValueError:
            return "Please enter correct number"

    return inner_func


def normalize(text):
    return text.lower()


# Парсер команд
@input_error
def parcer(text):
    line = text.split(" ")
    command = normalize(line[0])
    if command == "hello":
        return "Hi! How can I help you?"
    if command in ["good bye", "close", "exit"]:
        return "Good bye!"
    if command == "add":
        return add(f"{command} {line[1]} {line[2]}")
    if command == "change":
        return change(f"{command} {line[1]} {line[2]} {line[3]}")
    if command == "phone":
        return phone(f"phone {line[1]}")
    if command == "show" and normalize(line[1]) == "all":
        return get_phone_book()
    else:
        return "Unknown command, please try again"


# Добавление новых контактов
@input_error
def add(text):
    text = text.split(" ")
    if text[1] not in phone_book.keys():
        name = text[1]
        text[1] = Record(name)
        text[1].add_phone(text[2])
        phone_book.add_record(text[1])
    else:
        temp_rec = phone_book[text[1]]
        temp_rec.append_phone(temp_rec.phones, text[2])
        phone_book.add_record(temp_rec)

    return "Completed!"


# Изменение существующих контактов
@input_error
def change(text):
    text = text.split(" ")
    temp_rec = phone_book[text[1]]
    if text[2] in temp_rec.phones:
        temp_rec.change_phone(temp_rec.phones, text[2], text[3])
        phone_book.add_record(temp_rec)
    if text[2] not in temp_rec.phones:
        return "No such number in this record"
    return "Completed!"


# Достаём контак по имени
@input_error
def phone(text):
    text = text.split(" ")
    list = phone_book.data[text[1]].phones
    phones = ""
    for x in list:
        phones += x.value + " "
    return phones


# Вывод всей телефонной книги
def get_phone_book():
    result = ""
    for name, phone in phone_book.data.items():
        phones = ""
        for n in phone.phones:
            phones += n.value + " "
        result += "\n" + name + ": " + phones
    return result


# Основной модуль
def main():
    while True:
        user_input = input("Please enter your command: ")
        result = parcer(user_input)
        print(result)

        if result == "Good bye!":
            break


if __name__ == "__main__":
    main()
