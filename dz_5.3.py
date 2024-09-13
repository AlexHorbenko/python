import re
import string

user_print = input('Print: ') # 'Python Community' => #PythonCommunity
#'i like python community!' => #ILikePythonCommunity
#'Should, I. subscribe? Yes!' => #ShouldISubscribeYes

str = user_print.title()
str = ''.join(i for i in str if i not in string.punctuation)
str = re.sub(r'\W','', str)
str = '#' + str
if len(str) >= 140:
    print(str[:140])
