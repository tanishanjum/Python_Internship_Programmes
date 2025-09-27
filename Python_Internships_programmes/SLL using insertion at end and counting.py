class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def insertAtBegin(self,newdata):
        if self.head==None:
            newNode=Node(newdata)
            self.head=newNode
        else:
             newNode=Node(newdata)
             newNode.next=self.head
             self.head=newNode
    def display(self):
         if self.head==None:
             print('LL is Empty')
         else:
             temp=self.head
             while temp!=None:
                 print(temp.data)
                 temp=temp.next
    def insertAtEnd(self,newdata):
         if self.head==None:
             newNode=Node(newdata)
             self.head=newNode
         else:
             temp=self.head
             while temp.next!=None:
                 temp=temp.next
             newNode=Node(newdata)
             temp.next=newNode
    def counting(self):
        count=0
        if self.head==None:
            print(count)
        else:
            temp=self.head
            while temp!=None:
                count+=1
                temp=temp.next
            print('The count is: ',count)   
obj=SLL()
obj.insertAtBegin(100)
obj.insertAtBegin(200)
obj.insertAtBegin(300)
obj.insertAtBegin(400)
obj.insertAtBegin(500)
obj.insertAtEnd('Achuyth')
obj.insertAtEnd('karanam')
obj.display()
obj.counting()

            
