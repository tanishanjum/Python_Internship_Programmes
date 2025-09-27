n=int(input())
m=[]
for i in range(0,n):
    a=list(map(int, input().split()))
    m.append(a)
left_d=0
right_d=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            left_d=left_dom[i][j]
        if i+j==(n-1):
            right_d+m[i][j]
print(left_d, right_d)
