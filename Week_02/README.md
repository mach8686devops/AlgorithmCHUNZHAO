学习笔记


树的解法一般都是递归

因为都是树 一般情况下有非常强的重复性

重复性有最优重复性 最近重复性等

拆为左右子树

左右子树又可以无限往下继续拆分

从一般规律来看 递归是比较方便求解的


```python

def recursion(level, param1, param2, ...):   
    
    # recursion terminator     
    if level > MAX_LEVEL:
        process_result 	   
        return  
        
    # process logic in current level     
    process(level, data...)    
    
    # drill down     
    self.recursion(level + 1, p1, ...)     
    
    # reverse the current level status if needed
```


树本身是一种非线性的数据结构，循环遍历不易。当然循环遍历也是可以做，树是一种特殊的图，

可以使用图的广度优先遍历算法一层一层的循环遍历整棵树


```python
class Solution(object):
    def __init__(self):
        self.traverse_path = None

    # 前序  根左右
    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    # 中序  左根右
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    # 后序  左右根
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)
```



二叉树能实现增删查的功能，而散列表则可以更加高效的完成这些操作，为什么还要有二叉搜索树这样的数据结构呢？

第一，散列表中的数据是无序存储的，如果要输出有序的数据，需要先进行排序。而对于二叉查找树来说，我们只需要中序遍历，就可以在 O(n) 的时间复杂度内，输出有序的数据序列。
第二，散列表扩容耗时很多，而且当遇到散列冲突时，性能不稳定，尽管二叉查找树的性能不稳定，但是在工程中，我们最常用的平衡二叉查找树的性能非常稳定，时间复杂度稳定在 O(logn)。
第三，笼统地来说，尽管散列表的查找等操作的时间复杂度是常量级的，但因为哈希冲突的存在，这个常量不一定比 logn 小，所以实际的查找速度可能不一定比 O(logn) 快。加上哈希函数的耗时，也不一定就比平衡二叉查找树的效率高。
第四，散列表的构造比二叉查找树要复杂，需要考虑的东西很多。比如散列函数的设计、冲突解决办法、扩容、缩容等。平衡二叉查找树只需要考虑平衡性这一个问题，而且这个问题的解决方案比较成熟、固定。

最后，为了避免过多的散列冲突，散列表装载因子不能太大，特别是基于开放寻址法解决冲突的散列表，不然会浪费一定的存储空间。

综合这几点，平衡二叉查找树在某些方面还是优于散列表的，所以，这两者的存在并不冲突。我们在实际的开发过程中，需要结合具体的需求来选择使用哪一个

