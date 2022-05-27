# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def inOrderTraversal(root: Optional[TreeNode]) -> List[int]:
        a = []
        b = []
        c = root

        while c or a:
            while c:
                a.append(c)
                c = c.left
            c = a[-1]
            b.append(c.val)
            a.pop()
            c = c.right
