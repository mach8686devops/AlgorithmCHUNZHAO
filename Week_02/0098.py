class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 中序遍历
        def inOrder(root):
            res = []
            if root is None:
                return res
            res += inOrder(root.left)
            res.append(root.val)
            res += inOrder(root.right)
            return res

        result = inOrder(root)
        return False if result != sorted(list(set(result))) else True

    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True
