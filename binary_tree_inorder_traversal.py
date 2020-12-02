# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []
        self._inorderTraversal(root, arr)
        return arr
    
    def _inorderTraversal(self, root, arr):
        tmp = root
        if tmp:
            self._inorderTraversal(tmp.left, arr)
            arr.append(tmp.val)
            self._inorderTraversal(tmp.right, arr)
