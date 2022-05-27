# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        a = []
        pa = p
        qa = q
        while pa or a:
            while pa and qa:
                a.append(pa)
                if pa.val !=qa.val:
                    return False
                pa = pa.left
                qa = qa.left
            pa = a[-1]
            a.pop()
            pa = pa.right
            qa = qa.right
        return True

