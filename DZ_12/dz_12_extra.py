import math
from idlelib.configdialog import changes
from os import remove
from tracemalloc import Statistic

# **************************************** Task *******************************************

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def change_grade(self, new_grade):
        self.grade = new_grade
        return self.grade

    def __str__(self):
        return f"{self.name}, grade: {self.grade}"

student = Student('Alice', 90)
print(student)  # "Alice, grade: 90"
student.change_grade(95)
print(student)  # "Alice, grade: 95"


# ****************************************** Task *******************************************
# Створіть клас Dog, який має атрибути name (ім('я) та breed (порода).
# Додайте метод bark(), який виводить звук, що видає собака (наприклад, "Woof!").
# Додайте метод для виведення інформації про собаку.

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         return 'Woof!'
#
#     def __str__(self):
#         return f"{self.name}, a {self.breed}"
#
# my_dog = Dog('Buddy', 'Golden Retriever')
# my_dog.bark()  # "Woof!"
# print(my_dog)  # "Buddy, a Golden Retriever"

# ****************************************** Task *************************************************
# Створіть клас Book, який має атрибути title, author та pages.
# Додайте метод для підрахунку кількості прочитаних сторінок (передайте кількість прочитаних сторінок як аргумент).
# Додайте метод для виведення інформації про книгу.

# class Book:
#     def __init__(self, title, author, pages, readed = 0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.readed = readed
#
#     def read(self, add_pages):
#         self.readed += add_pages
#         return f"Прочитано {self.readed} сторінок"
#
#     def __str__(self):
#         return f"{self.title} by {self.author}, {self.pages} pages, {self.readed} pages read"
#
# my_book = Book('1984', 'George Orwell', 328)
# my_book.read(100)  # Прочитано 100 сторінок
# print(my_book)  # "1984 by George Orwell, 328 pages, 100 pages read"

# ****************************************** Задача ************************************************
# Створіть клас Car, який має такі атрибути: make (виробник), model (модель), year (рік випуску) та mileage (пробіг).
# Додайте метод, який повертає інформацію про автомобіль у вигляді рядка.

# class Car:
#
#     def __init__(self, make, model, year, mileage):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#
#     def __str__(self):
#         return f"{self.make}, {self.model}, {self.year}, {self.mileage} miles"
#
# car = Car('Toyota', 'Corolla', 2020, 15000)
# print(car)

# ******************************************************* Задача ***********************************
# Створіть клас MathOperations, який має статичний метод multiply, який приймає два аргументи і повертає їхню добуток.
# class MathOperations:
#
#     def __init__(self, *args):
#         self.args = args
#
#     @staticmethod
#     def multiply(a, b):
#         print(a * b)
#         return a * b
#
# MathOperations.multiply(3, 4) == 12

# *********************************** Задача 3 *******************************
# Створіть клас Circle, який має один атрибут radius та метод для обчислення площі круга.
# Наслідування: Створіть клас Cylinder, який наслідує від Circle і має додатковий атрибут height.
# Додайте метод для обчислення об'єму циліндра.
# *************************************** Варіант 1 ******************************************
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2
#
# class Cylinder(Circle):
#
#     def __init__(self, radius, height):
#         self.height = height
#         super().__init__(radius)
#
#     def volume(self):
#         return  self.area() * self.height
#
#
# circle = Circle(5)
# print(f"Area of circle: {circle.area()}")  # Площа круга
#
# cylinder = Cylinder(5, 4)
# print(f"Volume of cylinder: {cylinder.volume()}")  # Об'єм циліндра
#
#*********************************** Варіант 2***************************************
#
# import math
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return math.pi * self.radius ** 2  # Обчислення площі круга
#
#
# class Cylinder:
#     def __init__(self, circle, height):
#         self.circle = circle  # Зберігаємо об'єкт Circle
#         self.height = height  # Ініціалізація висоти
#
#     def volume(self):
#         return self.circle.area() * self.height  # Використовуємо метод area() з об'єкта Circle
#
#
# # Створення об'єкта Circle
# circle = Circle(5)  # Задаємо радіус
#
# # Створення об'єкта Cylinder, передаючи об'єкт Circle
# cylinder = Cylinder(circle, 4)  # Тут передається об'єкт Circle

# Обчислення обсягу циліндра
# print(f"Volume of cylinder: {cylinder.volume()}")  # Об'єм циліндра


# *********************************** Задача 2 ****************************
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return self.width * self.height
#
# # Перевірка:
# rect = Rectangle(5, 10)
# rect.calculate_area() == 50

#****************************************** Задача 1 ****************************
# Створіть клас Square, який успадковує клас Rectangle і має лише один атрибут side (сторона).
# Додайте метод calculate_area() так, щоб правильно обчислював площу квадрата.

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class Square(Rectangle):
#
#     def __init__(self, side):
#         super().__init__(side, side)
#         #Rectangle.__init__(self. side, side)
#
#     def calculate_area(self):
#         #return self.width * self.height
#         return self.width ** 2
#
# square = Square(5) #екземпляр класу
# square.calculate_area() == 25