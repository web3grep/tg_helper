def main():
    # Чтение строк от пользователя
    lines = []
    while True:
        line = input("Введите строку (или оставьте пустой для завершения): ")
        if line == "":
            break
        lines.append(line)

    # Запрос символа для разделения
    delimiter = input("Введите символ для разделения строк: ")

    # Разделение строк и сохранение результатов в списки
    split_lists = []
    for line in lines:
        parts = line.split(delimiter)
        # Расширение списка списков, если это необходимо
        while len(split_lists) < len(parts):
            split_lists.append([])
        # Добавление элементов в соответствующие списки
        for i, part in enumerate(parts):
            split_lists[i].append(part)

    # Сохранение списков в файлы
    for i, split_list in enumerate(split_lists, start=1):
        with open(f"split{i}.txt", "w") as file:
            for item in split_list:
                file.write(item + "\n")

    print("Списки сохранены в файлы.")

if __name__ == "__main__":
    main()
