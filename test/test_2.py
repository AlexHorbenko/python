import collections

text = '''When I was One I had just begun When I was Two I was nearly new '''
words = ['i', 'was', 'three', 'near']

text_list = text.lower().split()
print(text_list)
count_word_text = list(map(lambda x: text_list.count(x), text_list))
print(count_word_text)

# filter_word_text = filter(lambda x: x % 2 == 0, numbers)

united = list(zip(text_list, count_word_text))
print(united)

united_dict = dict(united)
print(united_dict)

# count_words = collections.Counter(text_list)
# print(count_words)
