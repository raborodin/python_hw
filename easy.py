# EASY
# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.
#
# код пишем тут...


# a = input('Введите a = ')
# print (list(str(a)))

# a = int(input('Введите a = '))
# while a > 0:
#     b = a % 10
#     a = int(a / 10)
#     print (b)

# a = int(input('Введите a = '))
# for (a  >  0, a):


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
# или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# a = input('Введите a = ')
# b = input('Введите b = ')
# print ('a = ', a)
# print ('b = ', b)
# c = a
# a = b
# b = c
# print ('a = ', a)
# print ('b = ', b)

# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

# yarse = int(input('Enter your age: '))
# if yarse < 18:
#     print('You need to grow up')
# else:
#     print('Come through')