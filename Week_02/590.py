# N叉树的后序遍历

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root, ]
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            res.append(node.val)
        return res[::-1]
