def greet_user(username):
    print("Hello " + username.title())

greet_user('Shriram')

# When you use default values, any parameter with a default value needs to be listed
# after all the parameters that don’t have default values. This allows Python to continue
# interpreting positional arguments correctly


def places(name, country='USA'):
    print('Name: ' + name + ' and country= ' + country)
    return 0


print(places('Shriram'))
places('Rama', 'Vaikuntha')
places(country='Norway', name='Magnus')


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
