import string

def is_palindrome(text):
    new_text = ""

    for char in text:
        if char not in string.punctuation:
            new_text += ''.join(char)

    new_text = new_text.replace(" ", "").lower()

    if new_text[::] == new_text[::-1]:
        result = True
    else:
        result = False
    return result

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")


#********************************* Variant 2 **************************************

#import re

#def is_palindrome(text):
    # Видаляємо всі символи, крім букв та цифр, і перетворюємо на нижній регістр
#    cleaned_text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    # Перевіряємо, чи є рядок паліндромом
#    return cleaned_text == cleaned_text[::-1]

# Тести
#assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
#assert is_palindrome('0P') == False, 'Test2'
#assert is_palindrome('a.') == True, 'Test3'
#assert is_palindrome('aurora') == False, 'Test4'

#print("ОК")