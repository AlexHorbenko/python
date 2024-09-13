import keyword

from Tools.scripts.verify_ensurepip_wheels import print_notice

user_text = input('Введіть текст:')
print(user_text)

a = ' ' in user_text
b = user_text.startswith('_')
c = user_text.islower()
d = user_text not in keyword.kwlist
e = user_text.count("_") <= 1
i = user_text[0].isdigit()
k = '_' in user_text
l = user_text[0].islower()
m = '!' in user_text

if b and e:
    print('True')
else:
    if c and k and i:
        print('True1')
    else:
        if l and a != 1 and c and d and m != 1:
            print('True2')
        else:
            print('False')


#_ #=> True
#__ #=> False
#___ #=> False
#x #=> True
#get_value #=> True
#some_super_puper_value #=> True
#assert_exception #=> True
#m3 #=> True
#3m #=> False
#get value #=> False
#Get_value #=> False
#get!value #=> False
#get_Value #=> False
#getValue #=> False
#assert #=> False

