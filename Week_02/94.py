class Solution:
    def postOrder(self, root):
        res = []
        if root is None:
            return res
        res += self.postOrder(root.left)
        res += self.postOrder(root.right)
        res.append(root.val)
        return res
