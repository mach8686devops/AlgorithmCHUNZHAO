class Solution:
    def mul(self, a, b):
        r = [[0, 0], [0, 0]]
        r[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        r[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1]
        r[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        r[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1]
        return r

    # 递归加速计算斐波那契数列 O(n^2) -> O(logn)
    def helper(self, n):
        from functools import reduce
        if n == 0:
            return [[1, 0], [0, 1]]
        if n == 1:
            return [[1, 1], [1, 0]]
        if n & 1 == 0:
            return self.mul(self.helper(n // 2), self.helper(n // 2))
        else:
            return reduce(self.mul, [self.helper((n - 1) // 2), self.helper((n - 1) // 2), [[1, 1], [1, 0]]])

    def climbStairs(self, n: int) -> int:
        return self.helper(n)[0][0]
