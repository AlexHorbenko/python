#***************************** Число *********************************
a = 3
print(a)
print(type(a)) # int - число, незмінний тип даних
b = int(3)
print(b)
print(type(b)) # int - число

#**************************** Кортеж *********************************
c = 'something', 'is', 'cool'
print(c)
print(type(c)) # tuple - кортеж, незмінний тип даних
c1 = 3,
print(c1)
print(type(c1)) # tuple - кортеж
c2 = (1, "hello", [3, 4, 5]) # tuple - кортеж
print(c2)
print(type(c2))

#******************************* Список ********************************
d = ['something1, is1, cool1']
print(d)
print(type(d)) # list - список, змінюваний тип даних
d1 = [1, 3.6, 9, "Hello", [2, "o"]]
print(d1)
print(type(d1))
d2 = list('Hello world')
print(d2)
print(type(d2))
d3 = list('something1, is1, cool1')
print(d3)
print(type(d3))
#********************************* Рядок ***********************************
e = ('something, is, cool')
print(e)
print(type(e)) # string - рядок

#********************************* Словник *****************************
f = {'something': '0', 'is': '1', 'cool': '2'}
print(f)
print(type(f)) # dict - словник
f1 = dict()
print(f1)
print(type(f1))
f2 = {}
print(f2)
print(type(f2))
f3 = dict(Life=1, Is=2, Cool=3)
print(f3)
print(type(f3))
f4 = [('IBM', 125), ('ACME', 50), ('PHP', 40)]
print(f4)
print(type(f4))
j = dict(f4)
print(j)
print(type(j))

#*************************************** Методи *******************************
#https://uk.from-locals.com/python-collections-counter/
