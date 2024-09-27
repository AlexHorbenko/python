first_number = float(input('Введіть перше число: '))
second_number = float(input('Введіть друге число: '))

action = int(input('Оберіть дію: додати числа: 1, відняти: 2, помножити: 3, розділити числа: 4   '))

sum = first_number + second_number
minus = first_number - second_number
multiple = first_number * second_number
divide = 'Ділення на нуль'

# print(first_number)
# print(second_number)

if action == 1:
    print(sum)
else:
    if action == 2:
        print(minus)
    else:
        if action == 3:
            print(multiple)
        else:
            if action == 4:
                if second_number == 0:
                    print(divide)
                else:
                    divide = first_number / second_number
                    print(divide)
            else:
                print('The end')

#*********** Second variation ******************

#if action == 1:
#    print(sum)
#elif action == 2:
#    print(minus)
#elif action == 3:
#    print(multiple)
#elif action == 4:
#    if not bool(second_number):
#        print(divide)
#    else:
#        divide = first_number / second_number
#        print(divide)
#else:
#    print('The end')