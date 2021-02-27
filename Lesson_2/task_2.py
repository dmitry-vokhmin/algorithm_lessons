"""
https://drive.google.com/file/d/1jHSfA2UFnBWrFj_rVvdFcT97LD11lLQ0/view?usp=sharing
Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

even = 0
odd = 0
x = str(input("Type in a natural number: "))

for i in x:
    if int(i) & 1:
        odd += 1
    else:
        even += 1

print(f"Even digits: {even}, odd digits: {odd}")
