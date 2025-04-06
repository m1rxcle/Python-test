"""# Задание №1

user_input = int(input("Введите целое число: "))

message = ""

if user_input > 0 and user_input % 2 == 0:
    message = "Положительное четное число"
elif user_input > 0 and user_input % 2 != 0:
    message = "Положительное нечетное число"
elif user_input < 0 and user_input % 2 == 0:
    message = "Отрицательное четное число"
elif user_input < 0 and user_input % 2 != 0:
    message = "Отрицательное нечетное число"
else:
    message = "Нулевое число"

print(message)"""

# Задание №2

user_word = input("Введите латинское слово: ").lower()

a_count = user_word.count("a")
e_count = user_word.count("e")
i_count = user_word.count("i")
o_count = user_word.count("o")
u_count = user_word.count("u")

# Проверка на наличие всех гласных
if a_count == 0 or e_count == 0 or i_count == 0 or o_count == 0 or u_count == 0:
    print("False")
else:
    odd_letters_count = a_count + e_count + i_count + o_count + u_count
    even_letters_count = len(user_word) - odd_letters_count

    a_output = f"встречается {a_count} раз(а)"
    e_output = f"встречается {e_count} раз(а)"
    i_output = f"встречается {i_count} раз(а)"
    o_output = f"встречается {o_count} раз(а)"
    u_output = f"встречается {u_count} раз(а)"

    result = f"Количество гласных букв: {odd_letters_count}.\nКоличество согласных букв: {even_letters_count}.\n'a' {a_output}\n'e' {e_output}\n'i' {i_output}\n'o' {o_output}\n'u' {u_output}"

    print(result)
