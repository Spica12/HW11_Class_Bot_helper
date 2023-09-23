from collections import UserDict

class Field:
    
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):

    # Реалізація класу
    pass


class Phone(Field):

    def __init__(self, value):
        self.check_validate(value)
    
    # Реалізація класу
    def check_validate(self, value):
        
        if value.isnumeric() and len(value) == 10:
            self.value = value
        else: 
            raise ValueError

    
class Record:
    
    def __init__(self, name: Name):
        self.name = Name(name)
        self.phones = []
    
    # Реалізація класу
    def add_phone(self, number: str)-> None:
        self.phones.append(Phone(number))

    def edit_phone(self, old_phone: str, new_phone: str)-> None:
        is_edited = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                is_edited = True

        # Якщо номера не існує, то викликається помилка  
        if not is_edited:
            raise ValueError


        # Не розумію, чого не працює наступни чином. 
        # Через index() не працює. Розумію, що в списку знаходиться об'єкт,
        # але як при цьому задіяти index() - ні(.
        # Працює тільки перебором в циклі for.
        # self.indx_phone = self.phones.index(old_phone)
        # self.phones[self.indx_phone].value = new_phone


    def find_phone(self, find_phone: str)-> Phone:
        for indx, phone in enumerate(self.phones):
            if phone.value == find_phone:
                return self.phones[indx]


        # Не розумію, як правильно використати метод index() в списку,
        # якщо елемент списку це об'єкт класу.
        # self.indx: int = self.phones.index()
        # return self.phones[self.indx]


              
            
    def remove_phone(self, remove_phone)-> None:
        for indx, phone in enumerate(self.phones):
            if phone.value == remove_phone:
                del self.phones[indx]
    
    def __str__(self):
        return f"Contact name: {self.name.value:<10}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):

    # Реалізація класу

    def add_record(self, record: Record)-> None:
        self.data[record.name.value] = record

    def delete(self, name)-> None:
        if name in self.data:
            del self.data[name]

    def find(self, name: str)-> Record:
        if name in self.data:
            return self.data[name]
        
    def show_all(self):

        if not self.data:
            return 'The phone dictionary is empty'
        else:
            self.result = 'The phone dictionary has next contacts:'
            for record in self.data:

                self.result += f"\nContact name: {record:<10}; phones: {'; '.join(p.value for p in self.data[record].phones)}"
            
            return self.result




if __name__ == '__main__':

    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record('John')
    john_record.add_phone('1234567890')
    john_record.add_phone('5555555555')

    # Додавання запису John до адресної книги
    book.add_record(john_record)


    # Створення та додавання нового запису Jane
    jane_record = Record('Jane')
    jane_record.add_phone('9876543210')


    print('--- Вивід всіх записів у книзі ---')
    book_info = book.show_all()
    print(book_info)


    print('--- Додавання запису без номеру ---')
    bob_record = Record('Bob')
    book.add_record(bob_record)

    book_info = book.show_all()
    print(book_info)

    print('--- Додавання номеру до Bob ---')
    bob: Record = book.find('Bob')
    print(bob)
    bob.add_phone('0986521232')

    book_info = book.show_all()
    print(book_info)


    print('--- Знаходження та редагування телефону для John ---')
    john = book.find('John')
    print(john)
    john.edit_phone('1234567890', '1112223333')

    # Виведення: Contact name: John, phones: 1112223333, 5555555555
    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone('5555555555')
    # Виведення: 5555555555
    print(f'{john.name}: {found_phone}')

    # Видалення запису Jane
    book.delete('Jane')
    book.show_all()

