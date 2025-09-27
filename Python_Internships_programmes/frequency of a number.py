arr=[1,6,3,3,1,2,4,1]
target=int(input('Enter:'))
d={}
for n in arr:
    if n not in d:
        d[n]=1
    else:
        d[n]+=1
print(d.keys(),d.values())
print(d[target])
