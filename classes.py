from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass

class Record():
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.record = {self.name.value: self.phones}

    def add_phone(self, phone):
        self.phones.append(phone)
        self.record = {Name: self.phones}

    def append_phone(self, new_phone):
        self.phones.append(new_phone)
        self.record = {Name: self.phones}

    def change_phone(self, old_phones, delete_phone, new_phone):
        for n in old_phones:
            if n.value == delete_phone:
                old_phones.remove(n)
                old_phones.append(new_phone)
        self.record = {Name: old_phones}

class AddressBook(UserDict):

    def add_record(self, record):
        temp_rec = {record.name.value: record}
        self.data.update(temp_rec)
