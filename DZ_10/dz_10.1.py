from inspect import isgenerator

def pow(x):
    return x ** 2

from inspect import isgenerator
def some_gen(begin, end, func):
    #list_gen = []
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        #list_gen.append(begin)
        count += 1

gen = some_gen(2, 4, pow)

#print(isgenerator(gen))
#print(list(gen))

assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')
