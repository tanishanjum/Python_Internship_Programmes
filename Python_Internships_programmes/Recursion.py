#Recursion The function which is call by itself is called recursion
def series(n):
    if n==5:
        return n
    else:
        print(n)
        return series(n+1)
print(series(1))    


 
