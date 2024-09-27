
def correct_sentence(text):

    length_sentense = len(text)
    last_sign = length_sentense - 1
    last_value = text[last_sign]

    if  last_value == '.':
        new_sentense = text
    else:
        new_sentense = text + '.'

    if text[0].islower():
        capitalize_letter = new_sentense.capitalize()
        print(capitalize_letter)
        return capitalize_letter
    else:
        print(new_sentense)
        return new_sentense

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
