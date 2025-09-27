#encapsulation: Binding data and function into single component is known as encapsulation
#class is an example of encapsulation
#Three access modifiers
#public data can be accessed any where
#-------------------------------------------------------
#AM        Inclass|outclass|InSubC1|outSubc1
#----------------------------------------------------
#public     yes     yes      yes     yes
#------------------------------------------------------------
#private    yes     no       no      no
#-----------------------------------------------------
#protected  yes     yes      yes     no
#-------------------------------------------------
#for private consider two underscores and for protected use single underscore
class ATM:
    def __init__(self):
      self.name='Achyuth'
      self.__pin=7890
      self._card='HDFC'
    
# Name mangling : private data can be accresed outside the class using mangling    
obj=ATM()
print(obj._ATM__pin)

    


    
