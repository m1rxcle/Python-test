# Задание №1

n_numbers = int(input("Введите количество чисел: "))

list_of_numbers = []

for i in range(1, n_numbers + 1):
    your_numbers = int(input("Введите число: "))
    list_of_numbers.append(your_numbers)

list_of_numbers.reverse()
print(list_of_numbers)


# Задание №2

n = int(input("Введите число: "))

numbers_list = []

for i in range(1, n + 1):
    your_values = int(input("Введите число: "))
    numbers_list.append(your_values)


def modified_list(list):
    last_element = list.pop()
    list.insert(0, last_element)
    return list


result = modified_list(numbers_list)
print(result)

# Задание №3

m = int(input("Введите максимальную массу для одной лодки: "))
n_ = int(input("Введите количество рыбаков: "))

all_fisherman_weights = []


for i in range(1, n_ + 1):
    weight_each_fisherman = int(input(f"Введите вес {i} рыбака: "))
    if weight_each_fisherman > m:
        raise ValueError(f"Недопустимый вес {i} рыбака ")
    all_fisherman_weights.append(weight_each_fisherman)

all_fisherman_weights.sort()

boats = 0
i = 0
j = n_ - 1

while i <= j:
    if all_fisherman_weights[i] + all_fisherman_weights[j] <= m:
        i += 1
    j -= 1
    boats += 1

print(f"Минимальное количество лодок: {boats}")
