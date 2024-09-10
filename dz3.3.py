initial_list = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
#initial_list = [1, 2, 3] #=> [[1, 2], [3]]
#initial_list = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#initial_list = [1] #=> [[1], []]
#initial_list = [] #=> [[], []]

if len(initial_list) == 0:
    zero_list = []
    initial_list.append(zero_list)
    print(initial_list * 2)
elif len(initial_list) % 2 == 0:
    half_list = len(initial_list) // 2
    first_list = initial_list[:half_list]
    second_list = initial_list[half_list:]
    new_list = []
    new_list.append(first_list)
    new_list.append(second_list)
    print(new_list)
elif len(initial_list) % 2 != 0:
    length_list = len(initial_list)
    new_list = []
    first_list = initial_list[:length_list // 2 + 1]
    second_list = initial_list[length_list // 2 + 1:]
    new_list.append(first_list)
    new_list.append(second_list)
    print(new_list)
else:
    len(initial_list) == 1
    new_list = []
    new_list.append(initial_list)
    print(new_list)


