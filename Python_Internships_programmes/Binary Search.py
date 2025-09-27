arr=list(map(int, input().split()))
tar=int(input())
arr=sorted(arr)
low=0
high=len(arr)-1
f=0
while low<=high:
    mid=(low+high)//2
    if tar==arr[mid]:
        f=1
        print(mid)
        break
    elif tar>arr[mid]:
        low=mid+1
    else:
        high=mid-1
if f==0:
    print(-1)
