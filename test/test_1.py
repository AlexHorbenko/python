import re


def first_word(text):
    # Замінюємо крапки і коми на пробіли
    text_edit = text.replace(".", " ").replace(",", " ")
    # Розбиваємо текст на слова, автоматично прибираючи зайві пробіли
    words = text_edit.split()
    print(words)
    # Шукаємо перше слово, що починається з літери
    for word in words:
        if re.match(r'^[a-zA-Z]', word):
            return word


# Тести
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
