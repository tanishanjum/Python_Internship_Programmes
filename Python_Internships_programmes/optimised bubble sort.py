#Optimised bubble Sort
a=[4,9,7,2,1]
swapped=False
n=len(a)
for i in range(1,n):
    for j in range(0,n-i):
        if a[j+1]<a[j]:
            swapped=True
            a[j+1],a[j]=a[j],a[j+1]
    if swapped==False:
        break
print(a)  
