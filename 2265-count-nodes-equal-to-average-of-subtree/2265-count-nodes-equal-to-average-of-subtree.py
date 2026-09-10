# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        matching_nodes = 0

        def post_order(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal matching_nodes
            if not node:
                return 0, 0
            
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)
            
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            
            if curr_sum // curr_count == node.val:
                matching_nodes += 1
                
            return curr_sum, curr_count

        post_order(root)
        return matching_nodes