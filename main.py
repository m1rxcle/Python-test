# Задание №1

pet_name = input("Введите имя питомца: ")

pets = {
    pet_name: {
        "Вид питомца": input("Введите вид питомца: "),
        "Возраст питомца": int(input("Введите возраст питомца(в годах): ")),
        "Имя владельца": input("Введите имя владельца: "),
    }
}

name = pet_name
type = pets[pet_name]["Вид питомца"]
age = pets[pet_name]["Возраст питомца"]
owner = pets[pet_name]["Имя владельца"]

if age == 1:
    right_pronouns = " год"
elif age > 1 and age < 5:
    right_pronouns = " года"
elif age >= 5 and age < 21:
    right_pronouns = " лет"
elif age > 21:
    right_pronouns = " года"

print(
    f"Это {type} по кличке '{name}'. Возраст питомца {age}{right_pronouns}. Имя владельца {owner}."
)


# Задание №2

my_dict = {}

for i in range(10, -6, -1):
    my_dict[i] = i**i

print(my_dict)
