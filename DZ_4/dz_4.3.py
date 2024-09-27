import random

initial_list = [1, 2, 3, 4, 5, 6, 7, 9] #== [1, 3, 7]
#initial_list = [1, 1, 2, 1] #== [1, 2, 2]
#initial_list = [6, 3, 7] #== [6, 7, 3]

initial_list = [random.randint(0, 10) for i in range(random.randint(3, 10))]
print(initial_list)
print([initial_list[0]] + [initial_list[2]] + [initial_list[-2]])
