from decimal import *
message = input("What is your name")
print(message+" is your name")

getcontext().prec=4
c = Context(prec=6, Emax=999, clamp=1)
setcontext(c)

prompt =''
prompt+= "Teel us your name"

age=int(input(prompt))
print(age)

if age %2==0:
    print('Your age is even')
else:
    print('Your age is odd')

message= 'Enter a number for the sum or -.5 to quit'

number = input(message)
number=float(number)
sum2=0
while number != -.5:
    sum2 += number
    print(number)
    number = input(message)
    number = float(number)
print("Sum is "+ str(sum2))

active= True

# while active:
#     message = input('Do you want to quit? Y/N')
#     if message == 'Y'.lower():
#         active=False
#         print('Bye Bye')

while active:
    message = input('Do you want to quit? Y/N')
    if message == 'Y'.lower():
        print('Bye Bye')
        break

for x in range(10):
    if x%2==0:
        continue
    else:
        print(x)

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    user = unconfirmed_users.pop()
    print('Verifying user ' + user.title() +" ...")
    confirmed_users.append(user)
print(confirmed_users)

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'dog' in pets:
    pets.remove('dog')
print(pets)

responses ={}

while active:
    name=input('What is your name?')
    response=input("What si favorite food")

    responses[name] = response

    repeat = input('Would you like to repeat? Y/N')

    if repeat == 'N':
        active = False

print(responses)