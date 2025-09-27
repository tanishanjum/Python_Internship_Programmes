#constructor: It is a special function which is used invoke(initialize)the instance
#types of constructor
#non-parameterized,parameterized,default
#parameterized: a constructor which contains parameters
#non-parameterized: a constructor which does not contains parameters
#default:a constructor created by a complier on its own
class Student:
    def __init__(self,name,roll,branch):
        self.name=name
        self.roll=roll
        self.branch=branch
    def displayDetails(self):
        print('Name is:',self.name)
        print('Roll is:',self.roll)
        print('branch is:',self.branch)
        print()
s1=Student('Aditya',101,'ISE')
s2=Student('Achyuth',63,'ECE')

s1.displayDetails()
s2.displayDetails()
