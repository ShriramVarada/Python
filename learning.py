players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])

players2=players[3:]
print(players2)

for player in players2[:3]:
    print(player.title())

players_copy=players[:]
# players_copy=players only tells players_copy point to the same list that players is pointing to

players_copy.insert(2, 'reed')
print(players_copy)

mahajanas=('prahlada', 'bali', 'suka', 'bhishma', 'narada', 'brahma',
           'siva', 'kaplia', 'janaka', 'kumaras', 'manu', 'yama')
print(mahajanas[-12:-4])

tuple2=(2,3,4)
print(tuple2)

tuple2=('dfs','sf')
print(tuple2)

if tuple2 != (2,3,3):
    print('They are not equal')

tuple2=3
print(tuple2)

for x in mahajanas:
    if x=='bali':
        print(x + " is the grandson of prahlada")
    elif x == 'narada':
        print('Devershi Narada')
    else:
        print(x.title())

x = 108
if x > 109 or x< 210: # and, not as well
    print('x <210 or x>109')

nondevotee = 'demons'

if nondevotee not in mahajanas:
    print(nondevotee.title()+"is not a devotee")

print(str(tuple2)+ " is a prime number")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

alien_0 = {'color': 'green', 'points': 5, 'speed' : 'Fast', 'sadf' : 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['god']='Jesus'
alien_0['color']='blue'

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

if alien_0['speed'].lower()== 'fast':
    print('It is fast')
    x_increment=100

print('alien_0 is ' + alien_0['speed'] + " " + str(x_increment))

del alien_0['color']
print(alien_0)

for key, value in alien_0.items():
    print('Key: '+ key + '\n')
    print('Value: ' + str(value) + '\n')

for keys in alien_0.keys():
    if keys == 'god':
        print(keys.title())

# if {'color' : 'green'} in alien_0:
#     print('is present')

for x in set(alien_0.values()):
    print(x)


