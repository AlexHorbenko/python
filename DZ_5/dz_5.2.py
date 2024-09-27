
while True:
    first_number = float(input('Введіть перше число: '))
    action = input('Оберіть дію: +, -, *, / ')
    second_number = float(input('Введіть друге число: '))

    if '+' in action:
        result = first_number + second_number
    elif '-' in action:
        result = first_number - second_number
    elif '*' in action:
        result = first_number * second_number
    elif '/' in action and second_number > 0:
        result = first_number / second_number
    else:
        result = 'Ділення на нуль'
        print(result)
    print(f'Результат: {result}')

    action1 = input('Плануєте продовжувати обчислення: так – y, ні – n: ')

    if action1 == 'n':
        break
print('End')

