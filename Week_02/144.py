class Solution:
    def preOrder(self, root):
        res = []
        if root is None:
            return res
        res.append(root.val)
        res += self.preOrder(root.left)
        res += self.preOrder(root.right)
        return res
