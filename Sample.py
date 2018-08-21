print("Hello")

namesofGod = ['Narayana', 'Krishna', 'Rama' , 'Govinda']

namesofGod.append('Narasimha')
print(namesofGod)

namesofGod.insert(2, 'Ajitah')
print(namesofGod)

del namesofGod[2]
print(namesofGod)

narayana = namesofGod.pop(0);
print(namesofGod)

govinda = 'Govinda'
namesofGod.remove(govinda)
print(namesofGod)

print(govinda.title())

namesofGod.sort()
print(namesofGod)

namesofGod.sort(reverse=True)
print(namesofGod)

print(sorted(namesofGod))
namesofGod.sort()
namesofGod.reverse()
print(namesofGod[-1]+'\n')

for name in namesofGod:
    print(name)

print('\n')

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")