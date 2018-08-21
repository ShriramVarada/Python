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

tuple2=3
print(tuple2)