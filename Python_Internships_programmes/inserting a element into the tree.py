def insertion(root, value):
    if root== None:
        return Node(value)
    else:
        if(value< root.data):
            root.left =insertion (root.left, value)
        elif value> root.data:
            root.right=insertion (root.right, value)
        else:
            return root
    return root

r=int(input('enter root node'))
root=Node(r)
root =insertion(root, 10)
