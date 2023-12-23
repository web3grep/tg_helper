def main():
    print("Введите строки (введите 'END' для завершения ввода):")
    lines = []
    while True:
        line = input()
        if line == 'END':
            break
        lines.append(line)

    text_a = input("Введите строку A: ")

    contains_a = []
    not_contains_a = []

    for line in lines:
        if text_a in line:
            contains_a.append(line)
        else:
            not_contains_a.append(line)

    print("\nСтроки, содержащие '{}':".format(text_a))
    for line in contains_a:
        print(line)

    print("\nСтроки, не содержащие '{}':".format(text_a))
    for line in not_contains_a:
        print(line)

if __name__ == "__main__":
    main()
