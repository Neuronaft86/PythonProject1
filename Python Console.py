
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return
    return x / y
print
print
print
print
print
print
choice = input
if choice in
    num1 = float(input
    num2 = float(input
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