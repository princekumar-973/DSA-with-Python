# Left -> Right -> Root
# Time Complexity = O(N)
# Space Complexity = O(H) H is Height of the Tree
# Worst case: O(N)
# Balanced tree: O(log N)

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        
        
def Postorder(root):
    if root is None:
        return
        
    Postorder(root.left)
    Postorder(root.right)
    print(root.val, end=" ")
    

    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
 
root.left.left = Node(4)
root.left.right = Node(5)
 
root.right.left = Node(6)
root.right.right = Node(7)
 
Postorder(root)
 
 
    
    