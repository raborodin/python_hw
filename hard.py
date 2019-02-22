# HARD
# Задание-1:
# Пользователь вводит число определите, является ли данное число простым. Делится только на себя и на единицу

# import math
#
# a = int(input('Enter a = '))
# for i in range(2, int(math.sqrt(a))):
#     if a % i == 0:
#         print('Composite number')
#     else:
#         print('Prime number')

# Задание-2
# Найдите n-ое число Фибоначчи

# d = int(input('введите номер числа в последовательности Фибоначчи: '))
# a = 0
# b = 1
# if d == 1:
#     print('Искомое числ:', a)
# elif d == 2:
#     print('Искомое числ:', b)
# else:
#     for i in range(3, d + 1, 1):
#         c = a + b
#         a = b
#         b = c
#     print(c)

# Задание-3
# Вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# (таких строк n, в каждой строке m троек AAA)

# n = int(input('Введите количество строк = '))
# m = int(input('Введите количество повторений AAA = '))
#
# a = 'AAABBB'
# b = 'BBBAAA'
#
# for n in range(1, n + 1, 1):
#     if n % 2 == 0:
#         print(b * m)
#     else:
#         print(a * m)