#set is a coolection of unordered elements
#syntax: n=set()
#Add is function used to insert the elements into the set
#intersection will retrun the duplicate elements
#difference will return the common elements
#Symmetric difference will return not common elememts
numbers={1,9,2,4,5}
n=set()
c=numbers.add(100)
print(numbers)


a={1,2,3}
b={1,7,8,2,3}
c=a.intersection(b)
print(c)

a={1,2,3}
b={1,7,8,2,3}
c=a.intersection(b)
print(c)

a={1,2,3}
b={1,7,8,2,3}
c=a.union(b)
print(c)

a={1,2,3}
b={1,7,8,2,3}
c=a.difference(b)
print(c)

a={1,2,3}
b={1,7,8,2,3}
c=a.symmetric_difference(b)
print(c)

