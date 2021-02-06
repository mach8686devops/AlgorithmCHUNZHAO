学习笔记


使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

此题如何默认为升序的排列 且无序的地方只有一个

也就是说 基本可以理解为按照某个位置进行了翻转的话

可以认为默认第一个元素是基准点 找到比这个小的值的索引位置 

```
        left,right=0,len(nums)-1
        target=nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid - 1] > nums[mid]:
                return mid
            if nums[mid] > target:
                left = mid + 1
            else:
                right = mid - 1
```


```
class Solution:
    def computePoint(self, points: List[int], target: int) -> int:
        a=self.left_bound(points,target)
        b=self.right_bound(points,target)
        return b-a+1 if a!=-1 and b!=-1 else 0
        
        
    def left_bound(self,points,target):
        if not points:
            return -1
        left,right=0,len(points)-1
        while (left<=right):
            mid=left+(right-left)//2
            if points[mid]<target:
                left=mid+1
            elif points[mid]>target:
                right=mid-1
            elif points[mid]==target:
                right=mid-1
        if left>=len(points) or points[left]!=target:
            return -1
        return left
    
    def right_bound(self,points,target):
        if not points:
            return -1
        left,right=0,len(points)-1
        while (left<=right):
            mid=left+(right-left)//2
            if points[mid]>target:
                right=mid-1
            elif points[mid]<target:
                left=mid+1
            elif points[mid]==target:
                left=mid+1
        if right <0 or points[right]!=target:
            return -1
        return right
        

```


一所学校的数学期中考试后，要对一个确定的成绩进行一个分段统计。

假设所有学生的考试成绩已经按照升序排列，那么需要做一个统计算法，输入一个特定分数，
求出这个分数的学生人数，要求算法时间复杂度 O(log n) 。

如果分数不存在，则返回 0。

示例 1：
输入： points = [51,70,70,81,81,100], target = 81
输出： 2

示例 2：
输入： points = [51,70,70,81,81,100], target = 60
输出： 0

