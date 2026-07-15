# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:      
        # This is onehundred percent the base case
        if not root:
            return []
      
        # the reason this works is because, you're traversing through the BST 
        # either branch will have a value of some sort, until it doesn't. 
        # the middle value of the recursive function, is "real" in the sense that it will 
        # always contain a value
        # once either branch reaches a base case it will return 
        # the reason that it works, is because it will "execute" in the order that it is written in 
        # more or less order of precendance is functions calls first, then addition. 
        # so all functions must be resolved before returning  
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

        # time complexity: 
        # O(n^2)
        # space complexity: 
        # O(n)
    

        
       


