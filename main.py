# Задание №1

n = int(input("Введите количество чисел: "))

equal_to_zero = 0

for i in range(n):
    n_numbers = int(input("Введите число: "))
    if n_numbers == 0:
        equal_to_zero += 1


print(f"Количество чисел равных нулю: {equal_to_zero}")

# Задание №2

x = int(input("Введите натуральное число: "))

divisors_count = 0

for i in range(1, x + 1):
    if x % i == 0:
        divisors_count += 1

print(f"Количество натуральных делителей: {divisors_count}")

# Задание №3

a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))


if a <= b:
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i, end=" ")
else:
    print("Второе число должно быть больше первого.")
