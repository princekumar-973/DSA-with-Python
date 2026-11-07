from collections import deque


# Complexity	
# Time	O(n)
# Space (including output)	O(n)
# Auxiliary space (excluding output)	O(n)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def BFS(root):
    if root is None :
        return []
    
    res = []
    queue = deque([root])
    
    while queue:
        
        level = []
        
        size  = len(queue)
        
        for i in range(size):
            node = queue.popleft()
            level.append(node.val)
            
            
            if node.left:
                queue.append(node.left)
                
            if node.right:
                queue.append(node.right)
                
                
        res.append(level)
            
    return res


    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
 
root.left.left = Node(4)
root.left.right = Node(5)
 
root.right.left = Node(6)
root.right.right = Node(7)
 
print(BFS(root))

        
    