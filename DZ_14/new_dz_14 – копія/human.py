__all__ = ('Human',)

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}\nAge: {self.age}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\n"
