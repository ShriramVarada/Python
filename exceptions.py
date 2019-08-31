while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    else:
        try:
            answer = float(first_number) / float(second_number)
        except ZeroDivisionError:
            print('Youc ant divide by zero')
        else:
            # Any code that depends on the try block executing successfully goes in the else block
            print(answer)

try:
    with open('alice.txt') as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg2 = 'File alice.txt could not be found'
    print(msg2)
else:
    print(contents)

titel = 'God consciousness'
print(titel.split())


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents2 = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
        pass  # do nothing and pass on
    else:
        # Count approximate number of words in the file.
        words = contents2.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filenames = ['alice', 'pizza\pi_digits']

for file in filenames:
    count_words(file)
