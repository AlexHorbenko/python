# Якщо потрібно додати виключення до кожного методу різних класів, це можна зробити таким чином:
# Створення користувацьких виключень:
# Якщо кожен метод вимагає специфічного виключення, можна створити різні класи виключень
# або один універсальний клас виключення для спільних помилок.
# Використання виключень у методах:
# У кожному методі слід перевіряти, чи відбувається ситуація, що вимагає виключення, та викликати його.
# Приклад для різних методів:

class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class ClassA:
    def method_a(self, value):
        if value > 10:
            raise CustomException("Value in ClassA exceeds the limit")
        return value

class ClassB:
    def method_b(self, value):
        if value < 0:
            raise CustomException("Negative value in ClassB is not allowed")
        return value

class ClassC:
    def method_c(self, value):
        if value == 0:
            raise CustomException("Value in ClassC cannot be zero")
        return value

# Використання try...except для кожного методу
try:
    obj_a = ClassA()
    obj_a.method_a(15)  # Викличе виключення
except CustomException as e:
    print(e)

try:
    obj_b = ClassB()
    obj_b.method_b(-5)  # Викличе виключення
except CustomException as e:
    print(e)

try:
    obj_c = ClassC()
    obj_c.method_c(0)  # Викличе виключення
except CustomException as e:
    print(e)
