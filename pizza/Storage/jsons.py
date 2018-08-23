import json

numbers = [2, 3, 4]
string1 = {'sfd': 'sdf'}

filename = 'test.json'

with open(filename, 'a') as file:
    json.dump(numbers, file)

with open(filename) as file:
    numbers = json.load(file)

print(numbers)
