import os

# Функция для добавления контакта
def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = surname + " " + name + " " + patronymic + " " + phone + "\n"
    
    # Открытие файла для добавления контакта
    with open("phonebook.txt", "a") as file:
        file.write(contact)

# Функция для вывода всех контактов
def print_all_contacts():
    # Проверка, существует ли файл с контактами
    if not os.path.exists("phonebook.txt"):
        print("Телефонная книга пуста")
        return
    
    # Открытие файла и вывод всех контактов
    with open("phonebook.txt", "r") as file:
        for line in file:
            print(line.strip())

# Функция для поиска контакта по фамилии
def find_contact_by_surname():
    surname = input("Введите фамилию для поиска: ")
    
    # Проверка, существует ли файл с контактами
    if not os.path.exists("phonebook.txt"):
        print("Телефонная книга пуста")
        return
    
    # Открытие файла и поиск контакта по фамилии
    with open("phonebook.txt", "r") as file:
        found = False
        for line in file:
            if surname.lower() in line.lower():
                print(line.strip())
                found = True
        if not found:
            print("Контакт с фамилией", surname, "не найден")

# Функция для изменения контакта
def edit_contact():
    surname = input("Введите фамилию контакта, который нужно изменить: ")
    new_name = input("Введите новое имя: ")
    new_surname = input("Введите новую фамилию: ")
    new_patronymic = input("Введите новое отчество: ")
    new_phone = input("Введите новый номер телефона: ")
    new_contact = new_surname + " " + new_name + " " + new_patronymic + " " + new_phone + "\n"
    
    # Открытие файла и поиск контакта по фамилии
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
    
    # Изменение контакта
    with open("phonebook.txt", "w") as file:
        for line in lines:
            if surname.lower() in line.lower():
                file.write(new_contact)
            else:
                file.write(line)

# Функция для удаления контакта
def delete_contact():
    surname = input("Введите фамилию контакта, который нужно удалить: ")
    
    # Открытие файла и поиск контакта по фамилии
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
    
    # Удаление контакта
    with open("phonebook.txt", "w") as file:
        for line in lines:
            if surname.lower() not in line.lower():
                file.write(line)

# Основная функция
def main():
    # Бесконечный цикл для работы с программой
    while True:
        print("1 - Добавить контакт")
        print("2 - Вывести все контакты")
        print("3 - Найти контакт по фамилии")
        print("4 - Изменить контакт")
        print("5 - Удалить контакт")
        print("6 - Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            print_all_contacts()
        elif choice == "3":
            find_contact_by_surname()
        elif choice == "4":
            edit_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Неправильный выбор")

if __name__ == "__main__":
    main()