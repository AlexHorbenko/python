
initial_list = [0, 1, 7, 2, 4, 8] #=> (0 + 7 + 4) * 8 = 88
#initial_list = [1, 3, 5] #=> 30
#initial_list = [6] #=> 36
#initial_list = [] #=> 0

new_list = initial_list.copy()
sum_elem = 0
result = 0
length_list = len(new_list)
last_value = length_list - 1

if len(initial_list) == 0:
    print(new_list)
else:
    for i in range(0, len(new_list), 2):
        sum_elem += new_list[i]
        result = sum_elem * new_list[last_value]
    print(result)

