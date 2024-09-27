import collections

def common_elements():
    initial_list = list(range(0, 101))
    list_one = []
    list_two = []
    set1_one = {}
    set2_two = {}

    for i, el in enumerate(initial_list):

        if el % 3 == 0:
            list_one.append(el)
            set1_one = set(list_one)

        if el % 5 == 0:
            list_two.append(el)
            set2_two = set(list_two)

    intersection_set = set1_one.intersection(set2_two)

    print(set1_one)
    print(set2_two)
    print(intersection_set)

    return intersection_set

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}


#******************************** Варіант 2 ***************************************
#def common_elements(start, end):
#    multiples_of_3 = {x for x in range(start, end) if x % 3 == 0}
#    multiples_of_5 = {x for x in range(start, end) if x % 5 == 0}
#    return multiples_of_3 & multiples_of_5

#assert common_elements(0, 100) == {0, 75, 45, 15, 90, 60, 30}
