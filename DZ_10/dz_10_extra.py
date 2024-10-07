def add_decorator(number):
    """
    Реалізує декоратор, який змінює поведінку функції, додаючи до результату функції число.

    :param number: Число для додавання.
    :return: Декоратор для додавання числа до результату функції.
    """
    def decorator(func):
		    # Ваш код

@add_decorator(5)
def example_function(x):
    return x * 2

# Перевірка
assert example_function(2) == 9