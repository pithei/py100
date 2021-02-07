import json

def read_data(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return data

def write_data(file_name, data_list):
    with open(file_name, "w") as f:
        json.dump(data_list, f)

def verify_record(persons_name, data_list):
    found = 0
    for record in data["birthdays"]:
        if ( record['name'] == persons_name ):
            print(f'Person {persons_name} was born on {record["birthday"]}')
            found = 1
    if ( found == 0 ):
        print(f'Person {persons_name} was not found in record list')
    return found

def add_record(data_list, file_name):
    new_person = {}
    new_person['name'] = input("Please enter persons name: ")
    new_person['birthday'] = input("Please enter persons birthday: ")
    person_exists = verify_record(new_person['name'], data_list)

    if ( person_exists ):
        print("Person exist in our data list, updating birthdate")
        #data_list["birthdays"].append(new_person)
        #write_data(file_name, data_list)
    else:
        data_list["birthdays"].append(new_person)
        #print(data_list)
        write_data(file_name, data_list)
    return data_list


FILE_NAME = "14_birthday_json.json"
data = read_data(FILE_NAME)

while True:
    user_decision = int(input("[1] - Search for name \n[2] - add new record \n"))
    if (user_decision == 1 ):
        print("searching for name")
        persons_name = input("Please enter persons name: ")
        verify_record(persons_name, data)
        break
    elif (user_decision == 2):
        print("adding record")
        add_record(data, FILE_NAME)
        break
    else:
        print("Invalid option, breaking the loop")
        break


"""
Solution, https://www.practicepython.org/solution/2017/02/25/34-birthday-json-solutions.html

import json

birthday = {}
with open('birthdays.json', 'r') as f:
          birthday = json.load(f)

def add_entry():
    name = input('Who do you want to add to the Birthday Dictionnary?\n').title()
    date = input('When is {} born?\n'.format(name))
    birthday[name] = date
    with open('birthdays.json', 'w') as f:
        json.dump(birthday, f)
    print('{} was added to my birthday list\n'.format(name))

def find_date():
    name = input("who's birthday do you want to know?\n").title()
    try :
        if birthday[name]:
            print('{} is born on {}\n'.format(name, birthday[name]))
    except KeyError:
        print('{} is not in the list\n'.format(name))

def list_entries():
    print('The current entries in my birthday list are:\n============================================')
    for key in birthday:
        print(key.ljust(31), ':', birthday[key])
    print()

while True:
    what_next = input('What do you want to do next? you can: Add, Find, List, Quit\n').capitalize()
    if what_next == 'Quit':
        print('Good Bye')
        raise SystemExit(0)
    elif what_next == 'Add':
        add_entry()
    elif what_next == 'Find':
        find_date()
    elif what_next == 'List':
        list_entries()
"""