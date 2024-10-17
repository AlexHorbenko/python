from exception import UserException
from group import Group
from student import Student

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
assert gr.find_student('Jobs') == st1

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!