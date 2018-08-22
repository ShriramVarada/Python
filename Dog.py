class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		print(self.name.title() + " is now sitting")
	
	def roll_over(self):
		print(self.name.title() + " is now rolling over")


my_dog = Dog('willie' , 6)
print("My dog name is "+ my_dog.name.title() + ".")