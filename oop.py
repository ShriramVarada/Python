class Person(object):

    def __init__(self, name, age, sex):
        self.name = name
        if type(age) is not int or age < 0:
            raise TypeError

        self.age = age
        self.sex = sex

    def __str__(self):
        return f'Person {self.name}'

    # Private methods - put a preceding underscore
    def _is_legal(self):
        return self.age >= 18

    # Python's solutions to static or class methods
    # `cls` is a reference to the current class
    @classmethod
    def hello(cls, age):
        print(f'Hello from {cls.__name__} and age is {age}')


foo = Person('Shriram', 20, 'Male')
print(foo.__str__())

foo.hello(3)


class Student(Person):

    def __init__(self, name, age, sex, university):
        super().__init__(name, age, sex)
        self.university = university
