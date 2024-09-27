def popular_words (text, words):

    text_list = text.lower().split()
    count_word_text = list(map(lambda x: text_list.count(x), words))
    united = list(zip(words, count_word_text))
    united_dict = dict(united)

    #print(united_dict)
    return united_dict


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
