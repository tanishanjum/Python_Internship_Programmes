a=[7,8,9,2,1]
n=len(a)
for i in range(0,n-1):
    t=a[i+1]
    j=i
    while j>=0 and t<a[j]:
        a[j+1]=a[j]
        j=j-1
    a[j+1]=t
print(a)    
