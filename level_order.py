# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        
        ret_list = []
        q = [root]
        
        while q:
            elem_list = []
            for i in range(len(q)):
                curr = q.pop(0)
                elem_list.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ret_list.append(elem_list)
            
        return ret_list
            
