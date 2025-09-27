h1=[6,5,14]
h2=[7,9,15]
h3=[3,12,1]
h1=h1[::-1]
h2=h2[::-1]
h3=h3[::-1]
sum1=sum(h1)
sum2=sum(h2)
sum3=sum(h3)
while True:
    min_height=min(sum1,sum2,sum3)
    if min_height<sum1:
        sum1-=h1.pop()
    elif min_height<sum2:
        sum2-=h2.pop()
    elif min_height<sum3:
        sum3-=h3.pop()
    elif sum1==sum2==sum3:
        print(sum1)
        break
