from collections import defaultdict
"""
Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль
(за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

comp = defaultdict(int)
total_prof = 0
less_avrg = []
more_avrg = []

n = int(input("How many companies ? "))

for _ in range(n):
    name = input("Name of the company: ")
    for quarter in range(1, 5):
        profit = int(input(f"Profit from {quarter} quarter: "))
        comp[name] += profit
        total_prof += profit

avrg = total_prof / n
print(f"The average profit: {avrg}")

for key, value in comp.items():
    if value >= avrg:
        more_avrg.append(key)
    elif value < avrg:
        less_avrg.append(key)

print("Profit more than average: ", *more_avrg)
print("*" * 50)
print("Profit less than average: ", *less_avrg)
