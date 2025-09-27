n=list(map(int,input().split()))
target=int(input())
c=0
for i in range(len(n)):
    if target==n[i]:
        c=1
        print(i)
        break
if c==0:
    print(-1)
