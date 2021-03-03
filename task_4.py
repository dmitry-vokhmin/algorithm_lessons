import random
"""
Определить, какое число в массиве встречается чаще всего.
"""

SIZE = 1000000
MIN_ITEM = 0
MAX_ITEM = 10000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

digit_dict = {}
max_count = 0
result = 0

for digit in array:
    if digit in digit_dict:
        digit_dict[digit] += 1
    else:
        digit_dict[digit] = 1

for key, value in digit_dict.items():
    if max_count < value:
        max_count = value
        result = key

print(f"The most repeated number: {result}, repeats: {max_count} times")
