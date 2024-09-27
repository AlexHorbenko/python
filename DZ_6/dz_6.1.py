import string

text = input('Введіть дві літери через дефіс: ')
ascii_list = string.ascii_letters

first_value = ascii_list.find(text[0])
last_value = ascii_list.find(text[2])
result = ascii_list[first_value:last_value+1]
print(result)

#************************** Варіант 2 (не певна чи є if  в даному випадку перевіркою на помилку) **********************

#if text[0] in ascii_list and text[2] in ascii_list:
#    first = ascii_list.index(text[0])
#    second = ascii_list.index(text[2])
#    result = ascii_list[first:second+1]
#    print(result)
