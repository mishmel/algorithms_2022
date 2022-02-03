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

Решите через рекурсию. Решение через цикл не принимается.

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
def number_of_digits(num = int(input('Введите любое натуральное число: ')), even = 0, not_even = 0):
    if num == 0:
        print(f' чётных чисел : {even}  не чётных чисел: {not_even}')
        return
    else:
        number = num % 10
        num = num // 10
        if number % 2 == 0:
            even += 1
        else:
            not_even += 1

        number_of_digits(num, even, not_even)

number_of_digits()
