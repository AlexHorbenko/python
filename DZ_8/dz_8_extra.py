# Створіть функцію calculate_circle_area, яка приймає радіус кола та повертає його площу.
# Використовуйте значення π (пі).
import math

# def calculate_circle_area(radius):
#     if radius == 0:
#         result = 0
#         print(result)
#         return result
#
#     s = math.pi * (radius ** 2)
#     result = round(s, 2)
#     print(result)
#     return result
#
# calculate_circle_area(0)
# calculate_circle_area(5)
# calculate_circle_area(10)
# calculate_circle_area(2.5)
# calculate_circle_area(7)

#**************************************** Задача 2 *******************************************
#Напишіть функцію find_gcd, яка приймає два числа та повертає їхній найбільший спільний дільник.
# def find_gcd(a, b):
#     if a % b == 0:
#         print(b)
#         return b
#     else:
#         return find_gcd(b, a % b)
#
# find_gcd(12, 18)
# find_gcd(15, 25)
# find_gcd(7, 11)
# find_gcd(30, 45)
# find_gcd(17, 23)

#*************************************** Задача 3 ***********************************************
# Напишіть функцію sum_of_digits, яка приймає ціле число та повертає суму його цифр.
def sum_of_digits(number):
    if number == 0:
        return number

    number = list(number)
    print(number)

sum_of_digits(123)
sum_of_digits(-456)
sum_of_digits(789)
sum_of_digits(0)
sum_of_digits(-9876)