n=int(input('Enter the tickets:'))
b=str(input('Enter the refreshment(k/q):'))
c=str(input('Enter the coupencode:'))

def discount(n):
    if n>=20:
        if n>20:
            newdiscount=n*(10/100)
            newdiscount=(2/100)*newdiscount
        else:
            print('no discount applicable')
def amount(c):
    if n=='k':
        print('k class')
    elif n==150:
        print('q class')
    else:
        print('enter the amount:')
        
def applydiscount(b):
    if b=='y':
        print('refreshment is added')
    else:
        print('refreshment is not added')
def calculateamount(n):
    if amount>n:
        claculate=newdiscount+applydiscount
    else:
        print('no discount')
print(discount(n))
print(amount(c))
print(applydiscount(b))
print(calculateamount(n))
            
            
            
