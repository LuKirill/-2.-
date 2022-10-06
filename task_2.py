"""
Задание 2.	Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""


def even_odd(n, i=0, j=0):
    residue = int(n) % 10
    n = int(n) // 10
    if residue % 2 == 0:
        i += 1
    else:
        j += 1
    if n > 0:
        return even_odd(n, i, j)
    else:
        return f'Количество четных цифр - {i} \n' \
               f'Количество нечетных цифр - {j}'


print(even_odd(input("Введите число: ")))
