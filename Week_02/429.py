# N叉树的层次遍历


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]  # 队列存储节点信息，层数
        res = [[]]  # 存储结果
        while queue:
            node, level = queue.pop(0)
            if len(res) <= level:
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level + 1))
        return res
