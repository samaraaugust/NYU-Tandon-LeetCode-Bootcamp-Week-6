# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        value = root

        while arr or value:
            while value:
                arr.append(value)
                value = value.left

            value = arr.pop()
            k -= 1

            if k == 0:
                return value.val

            value = value.right

        return -1
