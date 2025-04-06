# Задание №1

pet_type = input("Напишите вид питомца: ")
pet_age = int(input("Напишите возраст питомца(в годах): "))
pet_name = input("Напишите кличку вашего питомца: ")

right_pronans = ""

if pet_age == "1":
    right_pronans = "год"
elif pet_age > 1 and pet_age < 5:
    right_pronans = "года"
else:
    right_pronans = "лет"

print(f'Это {pet_type} по кличке "{pet_name}". Возраст: {pet_age } {right_pronans}.')

# Задание №2

first_stage = input(
    "Вам предстоит написать этапы развития человека по порядку.\nНапишите первый этап развития: "
)
second_stage = input("Напишите второй этап развития: ")
third_stage = input("Напишите третий этап развития: ")
fourth_stage = input("Напишите четвертый этап развития: ")
fivth_stage = input("Напишите пятый этап развития: ")
sixth_stage = input("Напишите шестой этап развития: ")
seventh_stage = input("Напишите седьмой этап развития: ")
eighth_stage = input("Напишите восьмой этап развития: ")
ninth_stage = input("Напишите девятый этап развития: ")
tenth_stage = input("Напишите десятый этап развития: ")
elevth_stage = input("Напишите одиннадцатый этап развития: ")
twelfth_stage = input("Напишите двенадцатый этап развития: ")

print(
    first_stage,
    second_stage,
    third_stage,
    fourth_stage,
    fivth_stage,
    sixth_stage,
    seventh_stage,
    eighth_stage,
    ninth_stage,
    tenth_stage,
    elevth_stage,
    twelfth_stage,
    sep="=>",
)
