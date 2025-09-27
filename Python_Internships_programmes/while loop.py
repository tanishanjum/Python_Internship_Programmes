n=5672
sum=0
while n>0:
    rem=n%10      #2    #7  #6
    sum=sum+rem   #2    #9  #15
    n=n//10   #567 #56
print(sum)
