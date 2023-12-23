import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Введите длину пароля: "))
    count = int(input("Сколько паролей сгенерировать: "))

    passwords = [generate_password(length) for _ in range(count)]

    print("\nСгенерированные пароли:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
