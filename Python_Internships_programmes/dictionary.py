numbers=[1,7,2,3,2,1,8,4,3,8,8]
d={}
for num in numbers:
    if num not in d.keys():
        d[num]=1
    else:
         d[num]+=1
for k,v in d.items():
    print(k,'->',v)
         
