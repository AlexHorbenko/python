<<<<<<< HEAD
import re

def first_word(text):
    text_edit = text.replace(".", " ").replace(",", " ")
    words = text_edit.split()
    for word in words:
        if re.match(r'^[a-zA-Z]', word):
            #print(word)
            return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
=======
import re

def first_word(text):
    text_edit = text.replace(".", " ").replace(",", " ")
    words = text_edit.split()
    for word in words:
        if re.match(r'^[a-zA-Z]', word):
            #print(word)
            return word


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
>>>>>>> c806f252d56869933894af54ad72e6d0ec98c5da
print('OK')