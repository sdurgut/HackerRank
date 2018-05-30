class Person:
	def __init__(self,first,last):
		self.first = first
		self.last = last
	def name(self):
		return self.first + " " + self.last

class Employee(Person):
	def __init__(self,first,last,staffnum):
		Person.__init__(self,first,last)
		self.staffnum = staffnum
	def getEmployee(self):
		return self.name() + " " + self.staffnum



x = Person("Orosbu","Cocugu")
y = Employee("Akilli", "Orosbu", "1212412")

print(x.name())
print(y.getEmployee())