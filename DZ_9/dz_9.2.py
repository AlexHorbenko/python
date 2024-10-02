<<<<<<< HEAD
def  difference (*args):
    data_list = list(args)

    if len(data_list) == 0:
        result = 0
        #print(result)
        return result

    min_num = []
    max_num = []
    for arg in data_list:
        min_num = min(data_list)
        max_num = max(data_list)
        result = max_num - min_num
        result = round(result, 2)
        #print(result)
        return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
=======
def  difference (*args):
    data_list = list(args)

    if len(data_list) == 0:
        result = 0
        #print(result)
        return result

    min_num = []
    max_num = []
    for arg in data_list:
        min_num = min(data_list)
        max_num = max(data_list)
        result = max_num - min_num
        result = round(result, 2)
        #print(result)
        return result

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
>>>>>>> 0d4d590d3a5386ab76d70f64408045785e16acb0
