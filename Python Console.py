#calculator222
# Функция для сложения
def add(x, y):
    return x + y

# Функция для вычитания
def subtract(x, y):
    return x - y

# Функция для умножения
def multiply(x, y):
    return x * y

# Функция для деления
def divide(x, y):
    if y == 0:
        return "Ошибка: деление на ноль!"
    return x / y

# Основная программа
print("Добро пожаловать в калькулятор!")
print("Выберите операцию:")
print("1. Сложение (+)")
print("2. Вычитание (-)")
print("3. Умножение (*)")
print("4. Деление (/)")

# Запрос выбора операции
choice = input("Введите номер операции (1/2/3/4): ")

# Проверка корректности ввода
if choice in ['1', '2', '3', '4']:
    # Запрос чисел у пользователя
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    # Выполнение выбранной операции
    if choice == '1':
        print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Результат: {num1} / {num2} = {divide(num1, num2)}")
else:
    print("Неверный ввод. Пожалуйста, выберите операцию от 1 до 4.")