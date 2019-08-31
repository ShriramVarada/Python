import json

username = input("enter a username")
filename = 'username.json'

with open(filename, 'w') as file:
    json.dump(username, file)

username = input("enter a username")
with open(filename) as file:
    if username == json.load(file):
        print('Hi we found you' + json.load(file))

# This is good practice: a function should either return
# the value you’re expecting, or it should return None.
