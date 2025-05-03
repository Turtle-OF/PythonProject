def calculator():
    print("Простий калькулятор")
    num1 = float(input("Введи перше число: "))
    operation = input("Операція (+, -, *, /): ")
    num2 = float(input("Введи друге число: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Ділення на нуль неможливе!"
    else:
        return "Невідома операція!"

    return f"Результат: {result}"

print(calculator())
