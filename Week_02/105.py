class Solution:
    def buildTree(self, preorder, inorder):
        if inorder == []:
            return None
        root = TreeNode(preorder[0])
        # print(preorder,inorder)
        x = inorder.index(root.val)  # 找到根在中序中的位置
        root.left = self.buildTree(preorder[1:x + 1], inorder[0:x])
        root.right = self.buildTree(preorder[x + 1:], inorder[x + 1:])
        return root
