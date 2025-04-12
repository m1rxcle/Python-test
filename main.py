# Задание №1
n = int(input("Введите кол-во чисел: "))

numbers = list(map(int, input("Введите числа через пробел: ").split()))

defference = set(numbers)

print(len(defference))

# Задание №2

n1 = int(input("Введите кол-во чисел для первого списка: "))
n1_list = set()

for i in range(n1):
    numbers_for_n1_list = int(input("Введите числа: "))
    n1_list.add(numbers_for_n1_list)


n2 = int(input("Введите кол-во чисел для второго списка: "))
n2_list = set()

for i in range(n2):
    numbers_for_n2_list = int(input("Введите числа: "))
    n2_list.add(numbers_for_n2_list)

equals = n1_list & n2_list

print(len(equals))


# Задание №3

user_input = list(map(int, input("Введите числа через пробел: ").split()))

existed = set()

for el in user_input:
    if el in existed:
        print("YES")
    else:
        print("NO")
        existed.add(el)
