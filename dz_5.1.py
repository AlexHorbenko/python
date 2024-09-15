import keyword
import string

user_text = input('Введіть текст:')
#print(user_text)

is_first_digit = user_text[0].isdigit()
is_lower = user_text.islower()
is_keyword = user_text in keyword.kwlist
has_single_underscore = '_' in user_text
has_double_underscore = user_text.count("__") > 0
has_forbidden_sign = False

has_forbidden_sign = any(char in string.punctuation.replace('_', '') or char == ' ' or char.isupper() for char in user_text)
has_double_underscore = '__' in user_text

result = True

if is_keyword:
    result = False

if is_first_digit:
    result = False

if not is_lower and user_text.count('_') > 1:
    result = False

if has_double_underscore and user_text != '_':
    result = False

if has_forbidden_sign:
    result = False

if user_text == '_':
    result =  True

print(result)


#_ #=> True
#__ #=> False
#___ #=> False
#get_value #=> True
#some_super_puper_value #=> True
#assert_exception #=> True
#3m #=> False

#get value #=> False
#get!value #=> False
#assert #=> False

#x #=> True
#m3 #=> True

#getValue #=> False
#Get_value #=> False
#get_Value #=> False

