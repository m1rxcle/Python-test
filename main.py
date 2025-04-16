# Задание № 1

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def recursive_print(l, index=0):
    if index == len(l):
        print("Конец списка")
        return

    print(l[index])
    recursive_print(l, index + 1)


recursive_print(my_list)
