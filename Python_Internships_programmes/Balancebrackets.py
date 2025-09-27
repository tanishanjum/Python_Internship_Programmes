s=str(input())
def balanceBracket(s):
    stack=[]
    opening=['(','[','{']
    dic={'(':')','[':']','{':'}'}
    for c in s:
        if c in opening:
            stack.append(c)
        else:
            top=stack[-1]
            if dic[top]==c:
                stack.pop()
    if stack==[]:
        return True
    else:
        return False
print(balanceBracket(s))n
