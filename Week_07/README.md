# 算法课程期末总结

主要的归纳收获

### 位运算

不断处以2 最低的在上面

左移动 <<
右移动 >>

或 ｜
与 &
取反 ～
异或 ^


x^0=x 
x^1s=~x  =~0 
x^-x=1s 
x^x=0 
c=a^b => 交换 a^c=b b^c=a
a^b^c=a^(b^c) 结合

不进位的加法

n位置清零 x&(~0<<n)
 (x>>n)&1 第n位值
 x&(1<<n)  幂值
 x|(1<<n) 置为1
 x&(~(1<<n)) 置为0
 x&((1<<n)-1) 最高位至n位清零
 
 奇偶 x&1==1
 /2 == >>1
 清低位1 x=x&(x-1)
 得到低位1 x&-x  
 
 
### 知识点分类总结

数组类
链表
栈
队列
哈希
set max

二叉树
bst 二叉搜索树
查询
递归
dfs/BFS
分治
回溯
贪心
二叉查找树


### dp 动态规划

动态规划的一般形式就是求最值

核心是穷举


存在重叠子问题
一般情况下需要备忘录或者dp table来优化穷举过程

也就是需要选择如何聪明的穷举

+ 问题的base case是什么
+ 有什么状态
+ 对于每个状态 可以做出什么选择使得状态改变
+ 定义dp数组来表现状态和选择

简单的例子让你把精力充分集中在算法背后的通用思想和技巧上

```
int fib(int N) {
    if (N==0) return 0;
    if (N==1 || N==2) return 1;
    int prev=1,curr=1;
    for (int i=3;i<=N;i++) {
        int sum=prev+curr;
        prev=curr;
        curr=sum;
    }
    return curr;
}


```


如何进行正确的状态压缩

一般递归或者迭代都可以

很多也可以叫做递推

动态规划一般可分为线性动规，区域动规，树形动规，背包动规四类。举例：

+ 线性动规：拦截导弹，合唱队形，挖地雷，建学校，剑客决斗等；
+ 区域动规：石子合并， 加分二叉树，统计单词个数，炮兵布阵等；
+ 树形动规：贪吃的九头龙，二分查找树，聚会的欢乐，数字三角形等；
+ 背包问题：01背包问题，完全背包问题，分组背包问题，二维背包，装箱问题，挤牛奶（同济ACM第1132题）等；


应用实例：最短路径问题 ，项目管理，网络流优化等；



首先定义状态，考虑有关的变量，然后进行定义
找出转移方程
进行优化，一般就是状态优化和转移优化。


```cpp
伪代码：
for i = 1 to n
    for j = W to w[i]
        dp[j] = max(dp[j], dp[j-w[i]] + v[i])

#include <iostream>
#include <cstring>
#define MAXN 10000
using namespace std;

int dp[MAXN];
int w[MAXN] = {0, 2, 1, 3, 2};
int v[MAXN] = {0, 3, 2, 4, 2};
int W = 5, n = 4;

int solve(int n, int W) {
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= n; i++) { // i从1开始，递增
        for (int j = W; j >= 0; j--) { // j按递减顺序填表
            if (j >= w[i]) {
                dp[j] = max(dp[j], dp[j-w[i]] + v[i]);
            }
        }
    }
    return dp[W];
}

int main() {
    cout << solve(n, W) << endl;
    return 0;
}

```


```python
# 62 题
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        #初始化放在for循环里了
        for i in range(0, m):#这个循环怎么走，应该根据状态转移方程来
            for j in range(0, n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

# 63
#动态规划问题
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        nums = obstacleGrid
        if m == 0 or n == 0:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
 
        #初始化放在for循环中
        for i in range(m):
            for j in range(n):
                if nums[i][j] == 1: #考虑障碍的位置，来分情况讨论（初始化）
                    continue
                if i == 0 and j == 0: #初始化
                    dp[i][j] = 1
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]                
        return dp[m-1][n-1]
        
# 55

class Solution:
    def canJump(self, nums) -> bool:
        size = len(nums)
        if size == 0:
            return True
 
        dp = [False for _ in range(size)]
 
        dp[0] = True
 
        for i in range(1, size):
            for j in range(i):
                if nums[j] >= i-j and dp[j]:
                    dp[i] = True
                    break
        return dp[size-1]
s = Solution()
print(s.canJump([2,2,1,0,4]))

# lintcode 397
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
 
    def longestIncreasingContinuousSubsequence(self, A):
        size = len(A)
        nums = A
        if size == 0:
            return 0
 
        dp = [0 for _ in range(2)]
 
        dp[0] = 1 #注意这个初始为1才对
        old, now = 0, 0
        max_value = dp[0]
        for i in range(1, size):
            old = now
            now = 1 - now
            if nums[i] > nums[i - 1]:
                dp[now] = dp[old] + 1
            else:
                dp[now] = 1
            max_value = max(max_value, dp[now])
        dp[0] = 1
        old, now = 0, 0
        for i in range(1, size):
            old = now
            now = 1 - now
            if nums[i] < nums[i - 1]:
                dp[now] = dp[old] + 1
            else:
                dp[now] = 1
            max_value = max(max_value, dp[now])
 
        return max_value


# 300
#状态表示的意义是：dp[i]表示以nums[i]为结尾的升序列长度，最后返回最大值
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         size = len(nums)
#         if size == 0:
#             return 0
        
#         dp = [0 for _ in range(size)]
#         #初始化
#         dp[0] = 1
 
#         for i in range(1, size):
#             dp[i] = 1
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)


# 定义一个数组pi，记录令当前dp[i]最大的那个j，也就是记录前一个数的索引,然后从后往前打印路径即可


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i]表示以i为结尾的最长上升子序列的长度
        #dp[i] = max(dp[j]+1, 1)
        if len(nums) == 0:
            return 0
        dp = [0 for _ in range(len(nums))]
 
        # dp[0] = 1
        pi = [0 for _ in range(len(nums))] #记录下来上一个是什么
        res = 0
        p = 0
        for i in range(len(nums)):
            dp[i] = 1
            pi[i] = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[j] + 1 == dp[i]:
                        pi[i] = j
            res = max(res, dp[i]) #记录下来最大值res极其索引p
            if dp[i] == res: 
                p = i
        seq = [0 for _ in range(res)]
        i = res - 1
        while i >= 0:
            seq[i] = nums[p]
            p = pi[p]
            i -= 1
        print(seq)

# 354
#这个题用排序算法无法通过
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        # envelopes.sort(key=lambda x: x[0])
        size = len(envelopes)
        if size == 0:
            return 0
         
        dp = [0 for _ in range(size)]
        
        dp[0] = 1
 
        for i in range(1, size):
            dp[i] = 1
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)


# 152

#用动态规划做，表明dp[i]表示以i结尾的连续序列的最大值。以i结尾时此刻不是最小就是最大值，因此维护max_value，min_value。
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        max_value = nums[0]
        min_value = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(max_value * nums[i], min_value * nums[i], nums[i])
            min_value = min(max_value * nums[i], min_value * nums[i], nums[i])
            max_value = dp[i]
        # print(dp)
        return max(dp)
        
# 64

class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        if m == 0:
            return 0
        
        dp = [[0 for _ in range(n)] for _ in range(2)]
        old, now = 0, 0
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, m):
            old = now
            now = 1 - now
            for j in range(n):
                dp[now][j] = float('inf')
                if i > 0:
                    dp[now][j] = min(dp[now][j], dp[old][j]+grid[i][j])
                if j > 0:
                    dp[now][j] = min(dp[now][j], dp[now][j-1]+grid[i][j])
        print(dp)
        return dp[now][n-1]

# 279
class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        
        for i in range(1, n+1):
            j = 1
            dp[i] = float('inf')
            while j*j <= i:
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        
        return dp[-1]

# 132
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        def isPalin(s): #先用动态规划算出是不是回文串表
            size = len(s)
            dp = [[False for _ in range(size)] for _ in range(size)]
            for j in range(size):
                i = j
                while i >= 0 and j < size and s[i] == s[j]:
                    dp[i][j] = True
                    i -= 1
                    j += 1
            for j in range(1, size):
                i = j - 1
                while i >= 0 and j < size and s[i] == s[j]:
                    dp[i][j] = True
                    i -= 1
                    j += 1
 
            return dp
        dp1 = isPalin(s)
 
        dp2 = [0 for _ in range(size+1)]
        dp2[0] = 0
 
        for j in range(1, size+1):
            min_value = float('inf')
            for i in range(j):
                if dp1[i][j-1]:#注意要和isPalin得出的矩阵对应
                    min_value = min(min_value, dp2[i] + 1)
            dp2[j] = min_value
 
        return dp2[size]-1

# 416
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #转化成这个列表中是否能找到元素和为sum/2——》即0-1背包问题
        #发现背包问题，如果元素只能使用一次，那么就把元素写入表格中
        #dp[i][j]表示前i个元素能否拼成j
        sum1 = sum(nums)
        if sum1 & 1 == 1:
            return False
        target = sum1 >> 1
        dp = [[False for _ in range(target + 1)] for _ in range(2)]
        old, now = 0, 0
        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            old = now
            now = 1 - now
            for j in range(target + 1):
                # i > 0 and j > 0
                dp[now][j] = dp[old][j] or (j - nums[i - 1] >= 0 and dp[old][j - nums[i - 1]])
        if dp[now][target]:
            return True
        return False

# 322
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if len(coins) == 0:
            return -1
        #最后一步，选哪个硬币 dp[i]为拼成i元所需最小的硬币数，由于硬币可以无限次取，所以考虑最后一步选哪个硬币
        #dp[i] = min(dp[i-coins[j]] + 1)状态转移方程为
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            dp[i] = float('inf')
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        # print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1

# 518

class Solution:
    def change(self, amount: int, coins) -> int:
        if amount == 0:
            return 1
        size = len(coins)
        if size == 0:
            return 0
 
        dp = [[0 for _ in range(amount + 1)] for _ in range(size + 1)]
        dp[0][0] = 1
        for i in range(1, size + 1):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
                
        # print(dp)
        return dp[size][amount]











```


### 排序

```python
def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        for j in range(1, n-i):    # 每轮找到最大数值
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j-1],arry[i]      #则交换两者
    return arry
```

两个优化

某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。

记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。

```python
def bubble_sort_opt(ary):
    n = len(ary)
    k = n    #k为循环的范围，初始值n
    for i in range(n):
        flag = True
        for j in range(1, k):    #只遍历到最后交换的位置即可
            if ary[j-1] > ary[j]:
                ary[j-1], ary[j] = ary[j-1], ary[j]
                k = j     #记录最后交换的位置
                flag = False
        if flag:
            break
    return ary
```


```python
def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary
```


```python
# 插入排序
def insert_sort(ary):
    count = len(ary)
    for i in range(1, count):
        key = i - 1
        mark = ary[i]
        while key >= 0 and ary[key] > mark:
            ary[key+1] = ary[key]
            key -= 1
        ary[key+1] = mark
    return ary
```

```python

def merge_sort(self, ary):

    if len(ary) <= 1:
        return ary

    median = int(len(ary)/2)    # 二分分解
    left = self.merge_sort(ary[:median])
    right = self.merge_sort(ary[median:])
    return self.merge(left, right)    # 合并数组

def merge(self, left, right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    res = []
    i = j = k = 0
    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res = res + left[i:] + right[j:]
    return res
```


```python
def quick_srot(ary):

    return qsort(ary, 0, len(ary)-1)

def qsort(ary, start, end):
    if start < end:
        left = start
        right = end
        key = ary[start]
        while left < right:
            while left < right and ary[right] >= key:
                right -= 1
            if left < right:    #说明打破while循环的原因是ary[right] <= key
                ary[left] = ary[right]
                left += 1
            while left < right and ary[left] < key:
                left += 1
            if left < right:    #说明打破while循环的原因是ary[left] >= key
                ary[right] = ary[left]
                right -= 1
            ary[left] = key    #此时，left=right，用key来填坑

        qsort(ary, start, left-1)
        qsort(ary, left+1, end)
    return ary
```


```python

def heap_sort(ary):
    n = len(ary)
    first = int(n/2-1)    #最后一个非叶子节点
    for start in range(first,-1,-1):    #构建最大堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):    #堆排，将最大跟堆转换成有序数组
        ary[end],ary[0] = ary[0], ary[end]    #将根节点元素与最后叶子节点进行互换，取出最大根节点元素，对剩余节点重新构建最大堆
        max_heapify(ary,0,end-1)    #因为end上面取的是n-1，故而这里直接放end-1，相当于忽略了最后最大根节点元素ary[n-1]
    return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True:
        child = root * 2 + 1    #调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and ary[child] < ary[child+1]:
            child = child + 1   #取较大的子节点
        if ary[root] < ary[child]:    #较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]    #交换
            root = child
        else:
            break
```

```python
def shell_sort(ary):
    count = len(ary)
    gap = round(count/2)    
    # 双杠用于整除（向下取整），在python直接用 “/” 得到的永远是浮点数，用round()得到四舍五入值
    while gap >= 1:
        for i in range(gap, count):
            temp = ary[i]
            j = i
            while j - gap >= 0 and ary[j-gap] > temp:    # 到这里与插入排序一样了
                ary[j] = ary[j-gap]
                j -= gap
            ary[j] = temp
        gap = round(gap/2)
    return ary
```



所有排序算法中最快的应该是桶排序(很多人误以为是快速排序,实际上不是.不过实际应用中快速排序用的多)但桶排序一般用的不多,因为有几个比较大的缺陷.

1.待排序的元素不能是负数,小数.

2.空间复杂度不确定,要看待排序元素中最大值是多少.

所需要的辅助数组大小即为最大元素的值.


冒泡 选择 插入

平均 最好 最差都是平方级别

堆 归并 快排（最差回到平方级别）

希尔排序平均在nlogn--n*n之间

外部排序

桶排序 计数排序 基数排序属于外部排序




参加课程 可能最大的收获

就是 一次不会 那就坚持五次

感谢各位老师的一路相助

继续不断面试 往大厂去试试吧






 
 
 
 


