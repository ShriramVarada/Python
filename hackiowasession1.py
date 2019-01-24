import requests
import string

r = requests.get('')


user_input = input()
print(user_input)

complex_var = 1+2j
scientific_not = 8e10

true = True
false = False

string1 = "fddf"

# Arrays as lists
empty_list = []

some_nums = [1,2,3,4]
some_types = [1, "42", True, [1, 5, 6]]

empty_dict = {}
fds = {
    'ads': 'dsf',
    'dsa': 324,
    2: 'kgj'
    }

print(2//3)
print(2/3)
print('Exponentiation', 2 ** 3)

print(1 in [1, 2, 3])
print('hello' in 'helloworld')

# in looks for the keys in the dictionaries not the values

print(type(fds))

# if, elif, else

for key, value in fds.items():
    print(key, value)

for index, item in enumerate([3, '53']):
    print(index, item)

print(string1[::2])

new_str = 'example.com/sad'

print(new_str.replace('.d', ' ').replace('m', 'fds'))
