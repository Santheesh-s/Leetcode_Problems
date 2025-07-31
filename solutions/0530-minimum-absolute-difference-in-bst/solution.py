# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def inorder(root):
            if root!=None:
                inorder(root.left)
                ls.append(root.val)
                inorder(root.right)
        ls=[]
        inorder(root)
        m=100000
        for i in range(1,len(ls)):
            if ls[i]-ls[i-1]<m:
                m=ls[i]-ls[i-1]
        return m
