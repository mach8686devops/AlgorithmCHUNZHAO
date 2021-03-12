# 两数之和
#  哈希表


class Solution:
    def twoSum(self, nums, target):
        mapping = {}
        for i, item in enumerate(nums):
            if (target - item) in mapping:
                return [mapping[target - item], i]
            mapping[item] = i
        # 注意是否有一定能够找到的条件
        # return [-1, -1]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
