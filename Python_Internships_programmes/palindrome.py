n=787
temp=n
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==temp:
     print('Palindrome')
else:
     print('not a palindrome')