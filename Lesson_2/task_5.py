"""
https://drive.google.com/file/d/1jHSfA2UFnBWrFj_rVvdFcT97LD11lLQ0/view?usp=sharing
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

s = ""
count = 0

for i in range(32, 128):

    if count == 10:
        print(f"{s}")
        count = 0
        s = ""
    else:
        s += f"'{chr(i)}'-{i} "
        count += 1

if count > 0:
    print(f"{s}")
