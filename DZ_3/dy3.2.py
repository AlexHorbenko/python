initial_list = [12, 3, 4, 10] #=> [10, 12, 3, 4]
#initial_list = [1] #=> [1]
#initial_list = [] #=> []
#initial_list = [12, 3, 4, 10, 8] #=> [8, 12, 3, 4, 10]


if not initial_list or 1 in initial_list:
    print(initial_list)
else:
    size_list = len(initial_list)
    value_elem = initial_list[size_list-1]
    initial_list.pop(size_list-1)
    initial_list.insert(0,value_elem)
    print(initial_list)

#************************* Варіант_2 ************************

#if len(initial_list) == 0 or 1 in initial_list:
#    print(initial_list)
#else:
#     size_list = len(initial_list)
#     value_elem = initial_list[size_list-1]
#     new_list = initial_list[0:size_list-1]
#     new_list.insert(0,value_elem)
#     print(new_list)
