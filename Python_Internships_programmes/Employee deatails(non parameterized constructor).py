class Employee:
    def __init__(self):
        self.name='Amogh'
        self.id=20243456
        self.role='Python developer'
        self.salary=78000.90
        self.company='Wipro'
    def display(self):
        print('name is :',self.name)
        print('id is :',self.id)
        print('role is :',self.role)
        print('salary is :',self.salary)
        print()

e1=Employee()
e2=Employee()
e1.display()
e2.display()


