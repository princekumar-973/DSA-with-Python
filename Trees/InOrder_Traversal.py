#Inorder Traversal (Left → Root → Right)
# Complexity Analysis
# - Time Complexity: O(N) – Every node is visited once.
# - Space Complexity: O(H) – Recursive call stack, where H is tree height.
# Remember this for interviews
# - Preorder: Root → Left → Right
# - Inorder: Left → Root → Right
# - Postorder: Left → Right → Root



class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


# Creating a binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Inorder traversal
inorder(root)
