import collections


# Задание №1
def find_factorial(n):
    if n == 0:
        return 1
    else:
        return n * find_factorial(n - 1)


factorial_list = []
number = 3
factorial = find_factorial(number)

for i in range(factorial, 0, -1):
    factorial_list.append(find_factorial(i))

print(factorial_list)

# Задание №2

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        },
    },
}


def create():
    last = collections.deque(pets, maxlen=1)[0]
    pet_name = input("Введите имя питомца: ")
    pets[last + 1] = {
        pet_name: {
            "Вид питомца": input("Введите вид питомца: "),
            "Возраст питомца": int(input("Введите возраст питомца: ")),
            "Имя владельца": input("Введите имя владельца: "),
        }
    }
    pets_list()


def read(id):
    if id not in pets.keys():
        return print("Такого питомца нет")

    pet_id = pets[id]
    name = list(pet_id.keys())[0]
    info = pet_id[name]

    return print(
        f"Это {info['Вид питомца']} по кличке \"{name}\". Возраст питомца: {info['Возраст питомца']} {get_suffix(info['Возраст питомца'])}. Имя владельца: {info['Имя владельца']}"
    )


def update():
    id = int(input("Введите id питомца информацию о котором хотите изменить: "))
    if id not in pets.keys():
        return print("Такого питомца нет")

    pet_name = input("Введите имя питомца: ")
    pets[id] = {
        pet_name: {
            "Вид питомца": input("Введите вид питомца: "),
            "Возраст питомца": int(input("Введите возраст питомца: ")),
            "Имя владельца": input("Введите имя владельца: "),
        }
    }
    print("Информация успешно обновлена!")
    read(id)


def delete():
    id = int(input("Введите id питомца которого хотите удалить: "))

    if id in pets.keys():
        del pets[id]
        print("Данные о питомце успешно удалены!")
        pets_list()

    else:
        return print("Такого питомца нет")


def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False


def get_suffix(age):
    if age == 1:
        return "год"
    elif age in [2, 3, 4]:
        return "года"
    elif age > 4 and age < 21:
        return "лет"
    else:
        return "года"


def pets_list():
    if len(pets) == 0:
        return print("Список питомцев пуст!")

    print("Список питомцев:")
    for pet_id in pets.keys():
        pet = get_pet(pet_id)
        name = list(pet.keys())[0]
        print(f'{pet_id}. "{name}".')


command = ""

while command != "stop":
    command = input("Введите одну из команд(create, read, update, delete, stop): ")

    if command == "create":
        create()
    elif command == "read":
        read_id = int(input("Введите id питомца: "))
        read(read_id)
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "stop":
        print("Программа завершена.")
        break
    else:
        print(
            "Неизвестная команда. Пожалуйста, введите одну из: create, read, update, delete, stop."
        )
