# with open('pizza\pi_digits') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

filename = 'pizza\pi_digits'
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in file_object:
        print(line.rstrip())

pi_digits=''
i=0
for line in lines:
    if i < 3:
        pi_digits += line.strip()
    i+=1

birthday = input('What is your birthday')

if birthday in pi_digits:
    print('Yay')
else:
    print('ooh')

print(float(pi_digits))


with open(filename, 'a') as file_object:
    file_object.write("\n I live\n")
    file_object.write("I love programming")