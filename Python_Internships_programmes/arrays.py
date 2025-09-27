#arrays
arr=[1,0,1,1,0,1,1,0]
ones=[]
zeros=[]
for n in arr:
    if n==0:
        zeros.append(n)
    else:
        ones.append(n)
print(zeros+ones)
print(len(zeros),len(ones))
#---------------------------------------
arr=[123,456,789]
for n in arr:
    s=str(n)
    print(s[::-1],end=' ')

