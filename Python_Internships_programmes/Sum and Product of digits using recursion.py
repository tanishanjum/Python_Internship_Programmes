#When ever base condition executes recursion breaks
# recursion work  under stack operation
def sumDigits(n):
    if n==0 or n==1:
        return 1
    else:
        return n%10+sumDigits(n//10)
print(sumDigits(984))


def proDigits(n):
    if n==0 or n==1:
        return 1
    else:
        return n%10*proDigits(n//10)
print(proDigits(984))


