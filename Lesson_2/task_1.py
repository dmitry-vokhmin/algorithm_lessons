"""
https://drive.google.com/file/d/1jHSfA2UFnBWrFj_rVvdFcT97LD11lLQ0/view?usp=sharing
Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
а запрашивает новые данные для вычислений. Завершение программы должно выполняться
при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
программа должна сообщать об ошибке и снова запрашивать знак операции.
Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.
"""

while True:
    x = int(input("Type in the first number: "))
    y = int(input("Type in the second number: "))
    z = input("Type in '0' for Exit or '+', '-', '*', '/' for calculations: ")

    if z == "*":
        print(f"{x} * {y} = {x * y}")
    elif z == "/":
        if y == 0:
            print(f"{x} cannot be divided by zero")
        else:
            print(f"{x} / {y} = {x / y}")
    elif z == "+":
        print(f"{x} + {y} = {x + y}")
    elif z == "-":
        print(f"{x} - {y} = {x - y}")
    elif z == "0":
        print("The game is over")
        break
