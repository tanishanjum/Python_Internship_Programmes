'''
Stack - Stack is a linear data structure.
Stack follows LIFO approach (Last In Fisrt Out)
Stack has one end(top).
Insertion and deletion can be posssibe from one end that is top.
Data can be deleted from stack from top end.
If stack is empty can't delete data.
It leads to stack underflow
If stack is full can't insert data.
It leads to stack overflow.
If top==-1 it means stack is empty.
'''

'''Operations on stack
1. PUSH - it is a function used to insert a data into stack.
2. POP - it is used to delete the data from the stack.
3. PEAK - it returns top most element from the stack.
'''

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self, data):
        self.stack.append(data)
        return self.stack
    
    def pop(self):
        if self.stack==[]:
            print("Stack underflow")
        else:
            self.stack.pop()
    
    def display(self):
        if self.stack==[]:
            print("Stack empty")
        else:
            for i in range(len(self.stack)-1, -1, -1):
                print(self.stack[i], end=" ")
    def peak(self):
        if self.stack==[]:
            print('no peak')
        else:
             print('peak ele:',self.stack[-1])

obj=Stack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()
obj.pop()
obj.peak()
obj.display()
