import random

def generate_random_number(lower_bound, upper_bound):
    if lower_bound > upper_bound:
        raise ValueError("Нижний предел должен быть меньше или равен верхнему пределу")

    random_number = random.uniform(lower_bound, upper_bound)
    return round(random_number, 6)

try:
    lower_bound = float(input("Введите нижний предел диапазона: "))
    upper_bound = float(input("Введите верхний предел диапазона: "))
    num_generations = int(input("Введите количество генераций: "))

    for _ in range(num_generations):
        random_number = generate_random_number(lower_bound, upper_bound)
        print(f"{random_number}")

except ValueError as e:
    print(f"Ошибка: {e}")
