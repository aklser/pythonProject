# Definition for a binary tree node.
from typing import Optional
import queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    q = queue.Queue()

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.ismirror(root, root)

    def ismirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val :
            return  self.ismirror(root1.left,root2.right) and self.ismirror(root1.right,root2.left)
        return False

