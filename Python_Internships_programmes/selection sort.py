a=[14,9,7,2,1]
n=len(a)
for i in range(0,n):
    s=a[i]
    pos=i
    for j in range(i+1,n):
        if s>a[j]:
            pos=j
            s=a[j]
    a[i],a[pos]=a[pos],a[i]
print(a)


