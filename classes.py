from collections import UserDict


class Field:
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    def __init__(self, phone):
        self.value = phone


class Record(Name, Phone):
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.record = {self.name: self.phones}

    def add_phone(self, phone):
        self.number = Phone(phone)
        self.phones.append(self.number)
        self.record = {self.name: self.phones}

    def append_phone(self, old_phones, new_phone):
        self.number = Phone(new_phone)
        self.phones = old_phones
        self.phones.append(self.number)
        self.record = {self.name: self.phones}

    def change_phone(self, old_phones, delete_phone, new_phone):
        self.new_phone = Phone(new_phone)
        for n in old_phones:
            if n.value == delete_phone:
                old_phones.remove(n)
                old_phones.append(self.new_phone)
        self.record = {self.name: old_phones}


class AddressBook(UserDict):
    data = {}

    def add_record(self, record):
        temp_rec = {record.name.value: record}
        self.data.update(temp_rec)

    def show_all(self):
        print(self.data)


def log():
    result = f"{Field.name}\n{Field.phones}\n{Field.record}"
    print(result)


if __name__ == "__main__":
    log()
