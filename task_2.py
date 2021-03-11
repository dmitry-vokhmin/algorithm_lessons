from collections import deque

"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

mapper = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
          "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

first = [char for char in input("Type in the first number: ")]
second = [char for char in input("Type in the second number: ")]


def digit_sum(first_num, second_num):
    result = deque()
    tmp = 0
    while first_num or second_num:
        n_first = mapper[first_num.pop()] if first_num else 0
        n_second = mapper[second_num.pop()] if second_num else 0
        s = n_first + n_second + tmp
        result.extendleft([key for key, value in mapper.items() if value == s % 16])
        tmp = s // 16
    if tmp:
        result.appendleft(str(tmp))
    print(result)

# Этот алгоритм слишком запутанный, но он работает
def digit_mul(first_num, second_num):
    result = deque()
    end = 2
    for i in range(len(second_num) - 1, -1, -1):
        tmp_mul = 0
        last_digit = end
        if result:
            for j in range(len(first_num) - 1, -1, -1):
                s = mapper[second_num[i]] * mapper[first_num[j]] + tmp_mul
                point = len(result) - last_digit
                if point >= 0:
                    new_sum = mapper[result[point]] + s % 16
                    result[point] = [key for key, value in mapper.items() if value == new_sum % 16][0]
                    tmp_sum = new_sum // 16
                else:
                    result.extendleft([key for key, value in mapper.items() if value == s % 16])
                    tmp_sum = 0
                tmp_mul = s // 16 + tmp_sum
                last_digit += 1
            if tmp_mul:
                result.extendleft([key for key, value in mapper.items() if value == tmp_mul])
            end += 1
        else:
            for j in range(len(first_num) - 1, -1, -1):
                s = mapper[second_num[i]] * mapper[first_num[j]] + tmp_mul
                result.extendleft([key for key, value in mapper.items() if value == s % 16])
                tmp_mul = s // 16
            if tmp_mul:
                result.extendleft([key for key, value in mapper.items() if value == tmp_mul])
    print(result)


digit_sum(first[::], second[::])
digit_mul(first, second)
