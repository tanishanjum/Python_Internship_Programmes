n=5672
pro=1
while n>0:
    rem=n%10
    pro=pro*rem 
    n=n//10
print(pro)