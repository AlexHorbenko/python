import math




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