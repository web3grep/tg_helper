import os

def rename_and_export_files(directory, current_first_number, new_first_number):
    offset = new_first_number - current_first_number
    new_directory = f"{directory}_new"
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)

    for i in range(current_first_number, current_first_number + 27):
        old_name = f"cookiebro-cookies ({i}).json"
        new_name = f"cookiebro-cookies ({i + offset}).json"
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(new_directory, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"Moved '{old_name}' to '{new_name}' in '{new_directory}'")
        else:
            print(f"File '{old_name}' not found")

def main():
    directory = input("Введите путь к папке: ")
    current_first_number = int(input("Введите текущий первый номер в файлах: "))
    new_first_number = int(input("Введите новый первый номер в файлах: "))
    rename_and_export_files(directory, current_first_number, new_first_number)

if __name__ == "__main__":
    main()
