"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [el ** 2 for el in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(inp_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == 'even':
        even_filter = filter(lambda x: x % 2 == 0, inp_list)  # фильтр четных
        even_list = [i for i in even_filter]
        return even_list

    elif filter_type == 'odd':
        odd_filter = filter(lambda x: x % 2 != 0, inp_list)  # фильтр не четных
        odd_list = [i for i in odd_filter]
        return odd_list

    elif filter_type == 'prime':
        prime_list = []
        for el in inp_list:
            int_div = list(range(el + 1))
            int_div2 = [divdr for divdr in int_div[2::] if el % divdr == 0]
            if len(int_div2) == 1:
                prime_list.append(el)
        return prime_list
