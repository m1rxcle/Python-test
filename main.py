# Задание №1

user_string = input("Введите строку: ").lower()

find_palendrom = user_string[::-1]

if find_palendrom == user_string:
    print("yes")
else:
    print("no")
