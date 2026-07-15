# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [] 
        res = []

        if root == None:
            return []

        curr_node = root    


        # Not sure if stack.pop() exist in python 
        # I caan re-check the logic, but it looks good right now as is.
        # push will insert the elements in front of the array, and append will insert in to the back
        # you have an infinte loop somewhere, something about how you wrote your algorithm, 
        # something about your while condition, is not good.

        # you might be able to set a value to none, to help with the while loop.

        # how about inside of nested if and elif, you simply just use ifs
        '''
        this algorithm only works for the first binary tree example.
        '''

        # this algorithm doesn't work for these three reasons 

        # Infinite Loop
        #Unnecessary Computations: Recomputing the same values repeatedly instead of storing them (e.g., in Dynamic Programming).
        while stack or curr_node:
                while curr_node:
                    stack.append(curr_node)
                    curr_node = curr_node.left
                curr_node = stack.pop()
                res.append(curr_node.val)
                curr_node = curr_node.right





        return res