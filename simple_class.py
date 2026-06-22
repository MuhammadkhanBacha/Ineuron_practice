class Student:
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setRoll(self, roll):
        self.roll = roll

    def getName(self):
        return self.name
    
    def getRoll(self):
        return self.roll
    
    def getAge(self):
        return self.age
    
    def display(self):
        print (f"Name: {self.name}")
        print (f"Age: {self.age}")
        print (f"Roll: {self.roll}")

object1 = Student("Muhammad", 18, 1223)
object1.display()