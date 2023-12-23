import os
import json
import glob
import pandas as pd

def find_tokens_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        ct0 = next((item['value'] for item in data if item.get('name') == 'ct0' and item.get('domain') == '.twitter.com'), None)
        auth_token = next((item['value'] for item in data if item.get('name') == 'auth_token' and item.get('domain') == '.twitter.com'), None)
        return auth_token, ct0

def main():
    folder_path = input("Введите путь к папке: ")
    json_files = glob.glob(os.path.join(folder_path, '*.json'))
    data = []

    for index, file in enumerate(json_files, start=1):
        auth_token, ct0 = find_tokens_in_file(file)
        data.append([index, auth_token, ct0])

    df = pd.DataFrame(data, columns=['Номер файла', 'Token Value', 'CT0 Value'])
    excel_file_name = 'export_tw_credentials.xlsx'
    df.to_excel(excel_file_name, index=False)
    print(f"Данные сохранены в файле {excel_file_name}")

if __name__ == "__main__":
    main()
