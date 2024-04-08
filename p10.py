# Особисті дані користувача
user_data = {
    "ID": 1,
    "Прізвище": "Петренко",
    "Ім'я": "Іван",
    "Група": "КН-25",
    "Курс": 2,
    "Книги (борг)": [],
    "Статистика книг": []
}

# Функція для виведення картки читача
def print_user_card(user):
    print("\nКартка читача:")
    for key, value in user.items():
        print(f"{key}: {value}")
    print()

# Функція для взяття книги у борг
def borrow_book(user, book_title):
    user["Книги (борг)"].append(book_title)
    print(f"\nКнига '{book_title}' успішно додана у борг.")

# Функція для повернення книги
def return_book(user, book_title):
    if book_title not in user["Книги (борг)"]:
        print(f"\nКнига '{book_title}' відсутня у списку боргу.")
    else:
        user["Книги (борг)"].remove(book_title)
        user["Статистика книг"].append(book_title)
        print(f"\nКнига '{book_title}' успішно повернена.")

# Основний код програми
while True:
    print("\nВиберіть опцію:")
    print("1. Вивести картку читача")
    print("2. Взяти книгу")
    print("3. Повернути книгу")
    print("0. Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print_user_card(user_data)
    elif choice == "2":
        book_title = input("Введіть назву книги, яку бажаєте взяти: ")
        borrow_book(user_data, book_title)
    elif choice == "3":
        if user_data["Книги (борг)"]:
            print("Список книг у боргу:", user_data["Книги (борг)"])
            book_title = input("Введіть назву книги, яку бажаєте повернути: ")
            return_book(user_data, book_title)
        else:
            print("У вас немає книг у боргу.")
    elif choice == "0":
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
