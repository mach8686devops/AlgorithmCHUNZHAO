class Solution:
    def inOrder(self, root):
        res = []
        if root is None:
            return res
        res += self.inOrder(root.left)
        res.append(root.val)
        res += self.inOrder(root.right)
        return res
