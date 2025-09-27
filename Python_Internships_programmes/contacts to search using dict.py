n=int(input('Enter n value:'))
contacts={}
for i in range(n):
      name,mobile=map(str,input().split(':'))
      contacts[name]=mobile
target=input('Enter name to search:')

if target in contacts.keys():
      print(contacts[target])
else:
    print('results not found')
