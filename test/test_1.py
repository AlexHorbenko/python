def generate_cube_numbers(end):
    list_gen = []
    for i in range(1, end+1):
        if int(i ** 3) <= end:
            list_gen += [i ** 3]
            yield i ** 3

from inspect import isgenerator

gen = generate_cube_numbers(1)

assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
