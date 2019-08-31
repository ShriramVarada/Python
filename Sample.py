print("Hello")

namesofGod = ['Narayana', 'Krishna', 'Rama' , 'Govinda']
print(namesofGod)

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

squares=[]

# for value in range(2,11,3):
#     squares.append(value**2)
squares = [value**2 for value in range(1,11)]
print(squares)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

print(min(squares))
print(max(squares))
print(sum(squares))