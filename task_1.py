import hashlib

"""
Определение количества различных подстрок с использованием хеш-функции. 
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
"""



def substring_sum(string):
    my_set = set()
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            my_set.add(hashlib.sha1(string[i:j].encode()).hexdigest())
    return len(my_set) - 2


print(substring_sum("abcb"))
