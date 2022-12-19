# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        finalList = []
        if root == None:
            return
        
        if root.left != None:
            leftNodes = Solution.inorderTraversal(self, root.left)
            for node in leftNodes:
                finalList.append(node)
            
        finalList.append(root.val)
        
        if root.right != None:
            rightNodes = Solution.inorderTraversal(self, root.right)
            for node in rightNodes:
                finalList.append(node)
            
        return finalList
