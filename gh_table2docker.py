import random

# Определение жилых часовых поясов
living_timezones = [-11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def transform_input_string(input_string):
    """
    Преобразует одну введенную строку в требуемый формат.
    
    Args:
    input_string (str): Строка введенная пользователем.

    Returns:
    str: Преобразованная строка.
    """
    # Разбиваем строку по табуляции
    parts = input_string.split('\t')
    # Добавляем случайный часовой пояс, исключая нежилые
    timezone = str(random.choice(living_timezones))
    # Преобразуем данные в требуемый формат
    transformed_string = ','.join(parts) + ',' + timezone
    
    return transformed_string

def main():
    # Чтение ввода от пользователя до пустой строки
    print("Введите строки данных, разделенные табуляцией (окончание ввода - пустая строка):")
    transformed_strings = []
    while True:
        input_string = input()
        if input_string == "":
            break
        transformed_string = transform_input_string(input_string)
        transformed_strings.append(transformed_string)
    
    # Вывод преобразованных строк
    for line in transformed_strings:
        print(line)

if __name__ == "__main__":
    main()
