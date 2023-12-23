def swap_characters(s, i, j):
    """ Функция для обмена символов в строке по индексам i и j. """
    if i >= len(s) or j >= len(s):
        return s
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def swap_words(s, i, j):
    """ Функция для обмена слов в строке по индексам i и j. """
    words = s.split()
    if i >= len(words) or j >= len(words):
        return ' '.join(words)
    words[i], words[j] = words[j], words[i]
    return ' '.join(words)

def process_line(line, A, B, C, D):
    """ Обработка строки в зависимости от её содержания. """
    if ' ' in line:  # Если строка содержит пробелы, считаем её seed фразой
        line = swap_words(line, A, B)
        line = swap_words(line, C, D)
    else:  # Иначе считаем строку хешем
        line = swap_characters(line, A, B)
        line = swap_characters(line, C, D)
    return line

def main():
    print("Введите строки (пустая строка для завершения ввода):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    while True:
        password = input("Введите 4-х значный PIN-код: ")
        if len(password) == 4 and all(c.isdigit() for c in password):
            break
        else:
            print("Неверный формат PIN-кода. Попробуйте снова.")

    A, B, C, D = [int(password[i]) - 1 for i in range(4)]

    for line in lines:
        processed_line = process_line(line, A, B, C, D)
        print(processed_line)

if __name__ == "__main__":
    main()
