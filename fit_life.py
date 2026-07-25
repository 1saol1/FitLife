import sys

# было выполнено через нейронку, т.к. не проходил тест
sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")


WATER_PER_KG = 30
ML_PER_L = 1000

print("Здравствуйте!")
print("Эта программа рассчитывает ваш индекс массы тела.")
print("Для корректной работы программы заполните несколько полей")

user_name = input("Введите свое имя: ")
user_age = int(input("Введите свой возраст: "))
user_weight = float(input("Введите вес (кг, например: 60.4): "))
user_height = float(input("Введите рост (м, например: 1.78): "))

# Рассчёт индекс массы тела с округлением до 1 знака
bmi = round(user_weight / (user_height ** 2), 1)

# Рассчитёт суточной нормы воды в миллилитрах
water_ml = user_weight * WATER_PER_KG

# Перевод миллилитры в литры
water_l = water_ml / ML_PER_L

print(f"Отчет для пользователя: {user_name.title()} ({user_age} г.)")
print(f"Ваш индекс массы тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l} л. в день")
print("\nРасчет окончен. Будьте здоровы!")
