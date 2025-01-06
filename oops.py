# class are user defined blueprint or prototype
#sum , multipluication,addition,constant
#Mthod , class variable , instance variables,constructor etc
#object for your classes

class Calculator:
    num = 100 #class variable

    # default constructor
    def __init__(self,a,b):
        self.firstNumber=a  #instance variable not a class variable
        self.secondNumber=b  #instance variable
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing  as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj=Calculator(4,5) # syntax to create object in python
obj.getData()
print(obj.Summation())
obj=Calculator(2,3) # syntax to create object in python

print(obj.Summation())

