# Задание №1

user_string = input("Введите строку: ").lower()

find_palendrom = user_string[::-1]

if find_palendrom == user_string:
    print("yes")
else:
    print("no")

# Задание №2

new_user_string = input("Введите строку: ")

if len(new_user_string) < 1000:
    trim_string = " ".join(new_user_string.split())
else:
    print("Длина строки превышает 1000 символов")

print(trim_string)
