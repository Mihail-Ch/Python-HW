


# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

phonebook =  dict()
keyContact = 0
file = 'Phonebook.txt'

def separator():
    print()
    print("---     ---     ---     ---")
    print()

# Write phonebook in file.txt
def write_contact_in_file():
    with open(file, 'w') as data:
        for key, value in phonebook.items():  
           data.write(f'Контакт номер: {key}   Фамилия: {value[0]}\n                   Имя: {value[1]}\n                   Телефон: {value[2]}\n')

# Add contact
def add_contact():
        lastN = input("Введите фамилию: ")
        firstN = input("Введите имя: ")
        phone = input("Введите телефон: ")
        separator()
        global keyContact
        keyContact = keyContact + 1
        phonebook[keyContact] = [lastN, firstN, phone]
        write_contact_in_file()
        
def print_data_contact(key, val):
    print(f'Контакт номер: {key}   Фамилия: {val[0]}')
    print(f'                   Имя: {val[1]}')
    print(f'                   Телефон: {val[2]}')
    
# Read phonebook
def read_phonebook():
    with open(file, "r") as data:
        for (key, value) in phonebook.items():
            dictionary = data.read()
            print_data_contact(key, value)
        return dictionary
        
# Search contact
def search_contact():
    lstName = input("Введите фамилию для поиска: ")
    print()
    for (key, value) in phonebook.items():
        if value[0] == lstName:
            print_data_contact(key, value)
    print()

# Change data
def change_data():
    pos_cont = int(input('Введите номер позиции контакта для изменений: '))
    phonebook[pos_cont]
    do_with_cont = int(input('Нажмите цифру соответствующую изменению:\n1 - изменить фамилию\n2 - имя\n3 - номертелефона\n4 - удалить\n'))
    if do_with_cont == 1:
        new_data = input('Введите новые данные: ')
        phonebook[pos_cont][0] = new_data
        write_contact_in_file()
    elif do_with_cont == 2:
        new_data = input('Введите новые данные: ')
        phonebook[pos_cont][1] = new_data
        write_contact_in_file()
    elif do_with_cont == 3:
        new_data = input('Введите новые данные: ')
        phonebook[pos_cont][2] = new_data
        write_contact_in_file()
    elif do_with_cont == 4:
            del phonebook[pos_cont]
            write_contact_in_file()
    
       


add_contact()
add_contact()
add_contact()
add_contact()
read_phonebook()
search_contact()
change_data()
read_phonebook()
change_data()
read_phonebook()





