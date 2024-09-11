
initial_list = [0, 1, 0, 12, 3] #-> [1, 12, 3, 0, 0]
#initial_list = [0] #-> [0]
#initial_list = [1, 0, 13, 0, 0, 0, 5] #-> [1, 13, 5, 0, 0, 0, 0]
#initial_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] #-> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]

i = 0
while i <= len(initial_list):
    first_index_zero = initial_list.index(0)
    initial_list.pop(first_index_zero)
    initial_list.append(0)
    i += 1
print(initial_list)


#********************** with 'copy()' *******************

#new_list = initial_list.copy()

#i = 0
#while i <= len(initial_list):
#    first_index_zero = new_list.index(0)
#    new_list.pop(first_index_zero)
#    new_list.append(0)
#    #print(new_list)
#    i += 1
#print(new_list)
#print(initial_list)
