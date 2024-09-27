def find_unique_value(some_list):
    el = [el for i, el in enumerate(some_list) if some_list.count(el) == 1]
    #print(el)
    return el

#******************************** Варіант 2 ********************************
#def find_unique_value(some_list):

#   for i, el in enumerate(some_list):
#      target = some_list.count(el)
#      if target == 1:
#         #print(el)
#   return el


assert find_unique_value([1, 2, 1, 1]) #== 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) #== 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) #== 0.5, 'Test3'
print("ОК")