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

while active:
    message = input('Do you want to quit? Y/N')
    if message == 'Y'.lower():
        active=False
        print('Bye Bye')