import math

user_number = float(input("Введіть п'ятизначне число:"))
number = int(user_number)
x = 10000
y = 1000
z = 100
i = 10
left_1, right = divmod(number, x)
left_2, right_1 = divmod(right, y)
left_3, right_2 = divmod(right_1, z)
left_4, right_3 = divmod(right_2, i)
#print(user_number)
#print(number)
#print(left_1, left_2, left_3, left_4, right_3)
#print(right_3, left_4, left_3, left_2, left_1)

new = right_3 * 10000 + left_4 * 1000 + left_3 * 100 + left_2 * 10 + left_1 * 1
print(new)
