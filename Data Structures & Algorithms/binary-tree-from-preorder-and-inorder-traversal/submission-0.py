# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : i for i, val in enumerate(inorder)}
        pre_idx = 0
        def construct(in_left, in_right):
            nonlocal pre_idx
            if in_left > in_right:
                return None
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx +=1

            index = inorder_map[root_val]
            root.left = construct(in_left, index - 1)
            root.right = construct(index + 1, in_right)
            return root
        return construct(0, len(preorder) - 1)