n=int(input())
for i in range(0,n):
    for j in range(0,n):
        if i==n//2 or j==n//2 or i==j or (i+j)==(n-1):
            print("*",end =" ")
        else:
            print(" ",end=" ")
    print()
