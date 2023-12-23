def get_sorted_list(list1, list2):
    # Создаем словарь для хранения соответствий IP и строк второго списка
    list2_dict = {}
    for item in list2:
        ip = item.split('@')[1].split(':')[0]
        list2_dict[ip] = item

    # Сортируем второй список в соответствии с порядком IP в первом списке
    sorted_list2 = [list2_dict[ip] for ip in list1 if ip in list2_dict]

    return sorted_list2

# Функция для безопасного ввода списка
def input_list(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines

# Запрашиваем ввод двух списков
list1 = input_list("Введите первый список IP-адресов, разделенных переносом строки (пустая строка для завершения):")
list2 = input_list("Введите второй список строк, разделенных переносом строки (пустая строка для завершения):")

# Получаем отсортированный второй список
sorted_list2 = get_sorted_list(list1, list2)

# Выводим результат
print("\nПереработанный второй список:")
for item in sorted_list2:
    print(item)
