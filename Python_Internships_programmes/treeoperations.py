#Trees:tree is a non linear data structure
#tree is a collection of nodes
#first node is always root node
#A root node has 2 childs leftchild and right child
#left and right are the pointers middle is the data
#properties of tree:
#1. Node: A node is a container which contain three part data,left,right
#2.Edge: A connection between one node another node is called edge
#3 Intermediate node: A node which have parent as well as child is called as intermediate node
#4.Leaf:A node which  doesnot contains parent and child either left or right
#5.Height: A longest connection between root to leaf node
#6.Level: It is the measure of counting each number of nodes present horizontally
#Types of trees:
#1. Binary tree: A node contains maximum of two children 0,1,2 for n nodes 2^n+1 -1 edges
#2.Complete tree: in complete binary tree where all the levels of a tree fill completely except leaf nodes which are filled as left as possible (2^n+1 -1)
#3.full binary tree: For a full binary tree every node has either two childs or zero childs
#4.perfect binary tree:A perfect binary tree all the nodes have two children 
#5.binary search tree:In binary search tree left children is left then the root and right tree is less than the root
# Tree traversal : there are three types of tree traversal
#1. preorder :Node->left->right
#2.inorder:left->Node->Right
#3.postorder:left->right->node
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.left.right=Node(50)
root.right.right=Node('BITM')

def preOrder(root):
    if root==None:
        return
    else:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)
preOrder(root)
def height(root):
    if root==None:
        return -1
    elif root!=None and root.left==None and root.right==None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1
print('the height is:',height(root))    
def count(root):
    if root==None:
        return 0
    elif root!=None and root.left==None and root.right==None:
        return 1
    else:
        lp=count(root.left)
        rp=count(root.right)
        return lp+rp+1
print('count is ',count(root))
def countLeaf(root):
    count=0
    if root==None:
        return 0
    elif root!=None and root.left==None and root.right==None:
        count+=1
        return count
    else:
          lp=countLeaf(root.left)
          rp=countLeaf(root.right)
          return lp+rp
print('countLeaf is ',countLeaf(root))        
        
        
