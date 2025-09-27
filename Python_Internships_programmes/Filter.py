#Filter Function
# Syntax Function name,variable
cgpa=[1.78,7.2,2.3,9.0,9.11]
def eligibleforplacements(cgpa):
    if cgpa>=8.1:
        return True
    else:
        return False
result=filter(eligibleforplacements,cgpa)
for i in result:
    print(i)
