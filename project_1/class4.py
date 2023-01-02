#classes
class Dog:
    numberoflegs = 4
    def eating(self, typeoffood):
        print(f'the dog is eating {typeoffood}')
    def walking(self):
        print(f'the dog is walking with its {self.numberoflegs} legs')

mydog = Dog()
mytypeoffood = "meat"
mydog.eating(mytypeoffood)
mydog.walking()

#initialization
class Dog2:
    """Class documentation goes here"""
    number_of_legs = 4 # class variable shared by
    def __init__(self, breed, age):
        self.breed = breed
        self.age = age
    def print_age(self):
        """it prints the age of the dog"""
        print("The dog is", self.age, "years old")

mydog2 = Dog2("dalmatian", 3)
mydog2.print_age()

#exercise
class Car:
    def __init__(self):
        self.distance = 0
    def move_forward(self):
        self.distance += 1
        return self.distance
        
mycar = Car()
mycar.move_forward()
mycar.move_forward()
mycar.move_forward()
distance = mycar.move_forward()

print(f"the car moved forward {distance} kms")

#inheritance
class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def getName(self):
        return self.firstname + " " + self.lastname
    def showInfo(self):
        print("The person is called", self.firstname, self.lastname)
    
class Employee(Person):
    def __init__(self, first, last, staffnum):
        super().__init__(first, last)
        self.staffnumber = staffnum
    def getEmployee(self):
        return self.getName() + ", " + self.staffnumber
    def showInfo(self):
        print("The employee is called", self.firstname, self.lastname)
    
a = Person("Marge", "Simpson")
b = Employee("Homer", "Simpson", "1007")
print(a.getName())
print(b.getName())
print(b.getEmployee())
print(a.showInfo())
print(b.showInfo())

#exercise
class Vehicle:
    def __init__(self):
        self.distance = 0
    
class Car2(Vehicle):
    def move_forward(self):
        self.distance += 1
        return self.distance

class RacingCar(Vehicle):
    def move_forward(self):
        self.distance += 2
        return self.distance
    
mycar2 = Car2()
mycar2.move_forward()
mycar2.move_forward()
mycar2.move_forward()
distance = mycar2.move_forward()
print(f"the car moved forward {distance} kms")

myracingcar = RacingCar()
myracingcar.move_forward()
myracingcar.move_forward()
myracingcar.move_forward()
distance = myracingcar.move_forward()
print(f"the racing car moved forward {distance} kms")

#multiple inheritance
class Person2:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last
    def getName(self):
        return self.firstname + " " + self.lastname
    def showInfo(self):
        print("The person is called", self.firstname, self.lastname)
        
class Consumer:
    def __init__(self, first, last, staffnum):
        self.firstname = first
        self.lastname = last
        self.staffnumber = staffnum
    def getConsumer(self):
        return self.firstname + ", " + self.staffnumber
    def showInfo(self):
        print("The consumer is called", self.firstname, self.lastname)
        
class Employee2(Person2, Consumer):
    def __init__(self, first, last, staffnum):
        Person2.__init__(self, first, last)
        Consumer.__init__(self, first, last, staffnum)
    def getEmployee(self):
        return self.getName() + ", " + self.staffnumber
    def showInfo(self):
        print("The employee is called", self.firstname, self.lastname)
    
a = Person2("Marge", "Simpson")
b = Consumer("Bart", "Simpson", "01")
c = Employee2("Homer", "Simpson", "07")
print(a.getName())
print(b.getConsumer())
print(c.getName())
print(c.getConsumer())
print(c.getEmployee())
print(a.showInfo())
print(b.showInfo())
print(c.showInfo())


#private
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')

#generate AttributeErrors:
# std = Student("Bill", 25)
# std.__schoolName
# std.__name
# std.__display()

#to see the private attributes and methods
std = Student("Bill", 25)
print(std._Student__name)
std._Student__name = 'Steve'
print(std._Student__name)
std._Student__display()

#static method
class Person3:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# a static method to check if a Person is adult or not.
	@staticmethod
	def isAdult(age):
		return age > 18

res = Person3.isAdult(22)
print(res)

person1 = Person3('mayank', 21)
print (person1.age)

#raise
x = 11

if not type(x) is int:
  raise TypeError("Only integers are allowed")

#exceptions
try:
    #x = int(input("Please enter a number:"))
    x = 9
    
    if(x>10):
        raise Exception ('The number must be less than 10')
    print(10/x)
    
except ZeroDivisionError:
    print("you tried to divide by zero")
except ValueError:
    print("it was not a numeric value")
except Exception as e:
    print(e)
else:
    print("good job")
finally:
    print("this is always printed")
    
    

