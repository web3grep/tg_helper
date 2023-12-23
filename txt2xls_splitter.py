import pandas as pd

def read_input():
    print("Введите текст (введите 'END' на новой строке для окончания ввода):")
    input_lines = []
    while True:
        line = input()
        if line == "END":
            break
        input_lines.append(line)
    return "\n".join(input_lines)

def process_text(text):
    # Разделение текста на строки и удаление пустых строк
    lines = [line for line in text.strip().split('\n') if line]

    # Разделение каждой строки на элементы
    data = [line.split(':') for line in lines]

    return data

def main():
    text = read_input()
    data = process_text(text)

    # Создание DataFrame
    df = pd.DataFrame(data)

    # Запись данных в Excel
    df.to_excel("output.xlsx", index=False)
    print("Данные сохранены в файл 'output.xlsx'.")

if __name__ == "__main__":
    main()