
def add_one(some_list):

    final_list = []
    list_of_number = ""

    #for char in some_list:
    #    list_of_number += str(char)

    list_of_number = "".join([str(y) for y in some_list])
    list_of_number = str(int(list_of_number) + 1)

    for char in list_of_number:
        final_list.append(int(char))
    print(final_list)
    return final_list

assert add_one([1, 2, 3, 4]) #== [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) #== [1, 0, 0, 0], 'Test2'
assert add_one([0]) #== [1], 'Test3'
assert add_one([9]) #== [1, 0], 'Test4'
print("ОК")
