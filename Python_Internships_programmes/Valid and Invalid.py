cse=int(input())
ece=int(input())
mech=int(input())
if cse<0 or ece<0 or mech<0:
    print('invalid')
elif cse==ece==mech:
    print('equal')
elif cse>ece and cse>mech:
    print('cse')
elif ece>cse and ece>mech:
    print('ece')
elif mech>cse and mech>ece:
    print('mech')
elif cse==ece:
    print('cse')
    print('ece')
elif mech==ece:
    print('mech')
    print('ece')
elif cse==mech:
    print('cse')
    print('mech')

