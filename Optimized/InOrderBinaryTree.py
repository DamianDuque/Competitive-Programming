## Recursive solution:

class Solution:
    def inorderTraversalRecursive(self, root):
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)
        return res  
    
## Iterative solution:

class Solution:
    def inorderTraversalIterative(self, root):
        res = []
        stack = []
        currentPointer = root

        while currentPointer or stack:

            while currentPointer:
                stack.append(currentPointer)
                currentPointer = currentPointer.left

            currentPointer = stack.pop()
            res.append(currentPointer.value)

            currentPointer = currentPointer.rigth
        return res