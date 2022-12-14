"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def func_2(n, summ=0, next=1):
    if n == 0:
        return summ
    summ += next
    next += 1
    n -= 1
    return func_2(n, summ, next)


def func_1(n):
    n2 = n * (n + 1) / 2
    n1 = func_2(n)
    if n2 == n1:
        print('Равенство выполняется')


func_1(2)
