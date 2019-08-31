def make(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("The size of the pizza is "+ str(size))
    for topping in toppings:
        print('- '+ topping)
# do not use print statements if importing this module
# in multiple other modules print('sfdfsd')