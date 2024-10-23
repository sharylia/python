import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 10))

print("Сгенерированный список чисел:", numbers)

user_input = int(input("Введите число от 1 до 10: "))

if user_input in numbers:
    print(f"Число {user_input} находится в списке.")
else:
    print(f"Число {user_input} не найдено в списке.")
