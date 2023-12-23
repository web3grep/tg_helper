def get_unique_lines_from_first_list():
    print("Введите строки первого списка (двойной Enter для завершения ввода):")
    first_list = []
    while True:
        line = input()
        if line == "":
            break
        first_list.append(line)

    print("Введите строки второго списка (двойной Enter для завершения ввода):")
    second_list = []
    while True:
        line = input()
        if line == "":
            break
        second_list.append(line)

    unique_lines = [line for line in first_list if line not in second_list]
    return unique_lines

# Запуск функции и вывод результата
unique_lines = get_unique_lines_from_first_list()
print("\nУникальные строки из первого списка:")
for line in unique_lines:
    print(line)
