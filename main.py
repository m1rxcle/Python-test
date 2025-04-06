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
