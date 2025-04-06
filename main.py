# Задание 1

first_side = float(input("Введите длину первой стороны: "))
second_side = float(input("Введите длину второй стороны: "))

area = round(first_side * second_side, 1)
perimeter = round((first_side + second_side) * 2, 1)

print(
    f"Площадь прямоугольника равна: {area}.\nПериметр прямоугольника равен: {perimeter}"
)

# Задание 2

initian_number = 46275

ten_thousands = initian_number // 10000
thousands = initian_number // 1000 % 10
hundreds = initian_number // 100 % 10
tens = initian_number // 10 % 10
ones = initian_number % 10

result = (tens**ones) * hundreds / (ten_thousands - thousands)


print(result)
