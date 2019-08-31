from pizza import make_pizza as pizza # as is used as alias
from collections import OrderedDict

def greet_user(username, password, age=''):
    print("Hello " + username.title())
    person={'username': username, 'password':password}
    if age:
        person['age']=int(age)
    return person


print(greet_user('Shriram', age=str(23), password='****'))

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


print(get_formatted_name('Shriram', 'Varadarajan'))


def print_list(list1):
    i = 1
    for item in list1:
        print('Item '+str(i)+": " + str(item))
        i += 1


print_list([2, 4, 'sfd'])


def print_models(unprinted_designs, completed_models):
    """
    Lists can be manipulated inside a function
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)


nprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(nprinted_designs[:], completed_models)
print(nprinted_designs, completed_models)

print_models(nprinted_designs, completed_models)
print(nprinted_designs, completed_models)


pizza.make(2, 'Jalapenos')


def make_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


print(make_profile('albert', 'einstein', location='princeton', field='physics'))
print(make_profile(last='sdf', location='princeton', field='physics', first='sfd', dfs='sfd'))


favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    # The order in which they were added
