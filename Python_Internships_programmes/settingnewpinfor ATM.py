class ATM:
    def __init__(self):
      self.name='Achyuth'
      self.__pin=7890
      self._card='HDFC'
      self.balance=50000
    def setPin(self,newpin):
        self.__pin=newpin
    def getPin(self):
        return self.__pin
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print('Withdraw successfully')
        else:
              print('insufficiant funds')
obj=ATM()
print('Old PIN')
print(obj.getPin())

obj.setPin(1234)
print('New PIN')
print(obj.getPin())
print(obj._ATM__pin)

obj.deposit(10000)
print(obj.balance)

obj.withdraw(20000)
print(obj.balance)
