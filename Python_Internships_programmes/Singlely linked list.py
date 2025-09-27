#linked list:it is a linear data structure
#it contains collection of node ,list node is head ,& last node is tail
#A node contains data and address of the next node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    head=None
one=Node(10)
two=Node(20)
three=Node(30)
four=Node(40)

head=one
one.next=two
two.next=three
three.next=four
four.next=None

temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next


