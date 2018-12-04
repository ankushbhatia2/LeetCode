# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxPathSumUtil(root):
    if root is None:
        return 0

    l = maxPathSumUtil(root.left)
    r = maxPathSumUtil(root.right)

    max_single = max(max(l, r) + root.val, root.val)

    max_top = max(max_single, l + r + root.val)

    maxPathSumUtil.msum = max(maxPathSumUtil.msum, max_top)
    return max_single


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxPathSumUtil.msum = -10 ** 10
        maxPathSumUtil(root)

        return maxPathSumUtil.msum