# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height(root) >= 0

    def height(self, root: TreeNode) -> int:
        # if root is None:
        #     return 0
        # lh, rh = self.height(root.left), self.height(root.right)
        # if lh >= 0 and rh >= 0 and abs(lh - rh) <= 1:
        #     return max(lh, rh) + 1
        # else:
        #     return -1

        if root is None:
            return 0
        rr, rl = self.height(root.right), self.height(root.left)
        if rl >= 0 and rr >= 0 and abs(rr - rl) <= 1:
            return max(self.height(root.left), self.height(root.right)) + 1
        else:
            return -1

