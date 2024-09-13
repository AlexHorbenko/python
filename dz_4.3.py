import random

initial_list = [1, 2, 3, 4, 5, 6, 7, 9] #== [1, 3, 7]
#initial_list = [1, 1, 2, 1] #== [1, 2, 2]
#initial_list = [6, 3, 7] #== [6, 7, 3]

new_list = initial_list.copy()

new_list = [random.randint(0, 100) for i in range(random.randint(3, 10))]
print(new_list)
print([new_list[0]] + [new_list[2]] + [new_list[-2]])

