# Задание 1

first_side = float(input("Введите длину первой стороны: "))
second_side = float(input("Введите длину второй стороны: "))

area = round(first_side * second_side, 1)
perimeter = round((first_side + second_side) * 2, 1)

print(
    f"Площадь прямоугольника равна: {area}.\nПериметр прямоугольника равен: {perimeter}"
)
