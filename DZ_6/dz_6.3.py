
initial_text = input('Введіть будь-яке ціле число: ')
str_to_list = list(initial_text)
final_list = str_to_list

while True:
    new_list = []
    result = 1

    for i, el in enumerate(final_list):
        new_list += el
        first_elem_newlist = new_list[i]
        int_list = int(first_elem_newlist)
        result = result * int_list
        str_list = str(result)
        final_list = list(str_list)

    if result <= 9:
        break
print(result)


#999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# потім 7 * 2 * 9 = 126,
# потім 1 * 2 * 6 = 12
# і в результаті 1 * 2 = 2
#1000 -> 0
#423 -> 8
#33 -> 9
#25 -> 0
#1 -> 1
