import os

def display_contacts(contacts):
    print("Телефонный справочник:")
    for contact in contacts:
        print(contact)

def save_contacts_to_file(contacts, filename):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(contact + '\n')

def search_contact(contacts, search_key):
    result = [contact for contact in contacts if search_key.lower() in contact.lower()]
    return result

def add_contact(contacts):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contact = f"{last_name} {first_name} {middle_name} - {phone_number}"
    contacts.append(contact)
    print("Контакт добавлен.")

def copy_contact(source_contacts, destination_contacts, index):
    try:
        contact_to_copy = source_contacts[index]
        destination_contacts.append(contact_to_copy)
        print("Контакт скопирован.")
    except IndexError:
        print("Некорректный индекс. Контакт не найден.")

def main():
    contacts = []

    while True:
        print("\nВыберите действие:")
        print("1. Вывести контакты")
        print("2. Сохранить контакты в файл")
        print("3. Поиск контакта")
        print("4. Добавить контакт")
        print("5. Копировать контакт из одного файла в другой")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            filename = input("Введите имя файла для сохранения: ")
            save_contacts_to_file(contacts, filename)
            print(f"Контакты сохранены в файл {filename}")
        elif choice == '3':
            search_key = input("Введите ключ для поиска: ")
            search_result = search_contact(contacts, search_key)
            if search_result:
                print("Результаты поиска:")
                display_contacts(search_result)
            else:
                print("Контакт не найден.")
        elif choice == '4':
            add_contact(contacts)
        elif choice == '5':
            source_filename = input("Введите имя файла, откуда копировать контакт: ")
            try:
                with open(source_filename, 'r') as source_file:
                    source_contacts = source_file.read().splitlines()
                index_to_copy = int(input("Введите номер строки для копирования: "))
                copy_contact(source_contacts, contacts, index_to_copy - 1)
            except FileNotFoundError:
                print("Файл не найден.")
        elif choice == '6':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")

    print("Программа завершена.")

if __name__ == "__main__":
    main()
