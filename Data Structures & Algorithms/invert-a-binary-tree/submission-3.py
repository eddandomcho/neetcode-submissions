# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return None
        if root.left and node.right:
            node.left, node.right = node.right, node.left
            self.invertTree(node.left)
            self.invertTree(node.right)
        elif node.left and not node.right:
            self.invertTree(node.left)
            node.right = node.left
            node.left = None
        elif node.right and not node.left:
            self.invertTree(node.right)
            node.left = node.right
            node.right = None
        return root
            
