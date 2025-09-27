#the amount of time taken by the algorithm to execute is called time complexicity
#TC  for DLL inserting at end has order of 1
#TC for SLL inserting at end has order of n
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertAtbegin(self,newdata):
        if self.head==None or self.tail==None:
            newNode=Node(newdata)
            self.head=newNode
            self.tail=newNode
        else:
            newNode=Node(newdata)
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode
    def insertAtend(self,newdata):
        if self.head==None or self.tail==None:
            newNode=Node(newdata)
            self.head=newNode
            self.tail=newNode
        else:
            newNode=Node(newdata)
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
    def deleteAtbegin(self):
        if self.head is None:
            print('DLL is empty')
        else:
            if self.head == self.tail:  # Only one node in the list
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None        
    def display(self):
        if self.head==None or self.tail==None:
            print('DLL is empty')
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
    def            
obj=DLL()
obj.insertAtbegin(100)
obj.insertAtbegin(200)
obj.insertAtbegin(300)
obj.insertAtbegin(400)
obj.insertAtbegin(500)
obj.insertAtend('Aditya')
obj.insertAtend('Achyuth')
obj.display()
	
