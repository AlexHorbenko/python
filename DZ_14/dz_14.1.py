class UserException(Exception):
    def __init__(self, message):
        self.message = message

    def get_exception_message(self):
        return self.message

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Gender: {self.gender}\nAge: {self.age}\nFirst Name: {self.first_name}\nLast Name: {self.last_name}\n"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}Record Book: {self.record_book}\n"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        max_amount = 10
        if len(self.group) >= max_amount:
            raise UserException("Додали 11 студента")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        else:
            return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student)
        return f'Number: {self.number}\n{all_students}'

# person = Human("Male", 30, "John", "Doe")
# print(person)
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# print(st1)
# print(st2)
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)

try:
    for i in range(9):
        gr.add_student(Student('Male', 44, f'Student{i}', f'Lastname{i}', f'AN{i}'))
except UserException as error:
    print(error)

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

# print(Group.mro())