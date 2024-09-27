text = '''When I was One I had just begun When I was Two I was nearly new '''
words = ['i', 'was', 'three', 'near']

text_list = text.lower().split()
print(text_list)

#count_word_text = list(map(lambda x: text_list.count(x), text_list))
count_word_text = list(map(lambda x: text_list.count(x), words))
print(count_word_text)

united = list(zip(words, count_word_text))
print(united)
united_dict = dict(united)
print(united_dict)
