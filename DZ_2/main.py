import math

user_number = float(input('Введіть чотиризначне число:'))
number = int(user_number)
x = 1000
y = 100
z = 10
left_1, right = divmod(number, x)
left_2, right_1 = divmod(right, y)
left_3, right_2 = divmod(right_1, z)
#print(user_number)
#print(number)
print(left_1)
print(left_2)
print(left_3)
print(right_2)
