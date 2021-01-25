# 丑数


class Solution:
    def nthUglyNumber(self, n: int) -> int:

        # dp, a, b, c = [1] * n, 0, 0, 0
        # for i in range(1, n):
        #     n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
        #     dp[i] = min(n2, n3, n5)
        #     if dp[i] == n2: a += 1
        #     if dp[i] == n3: b += 1
        #     if dp[i] == n5: c += 1
        # return dp[-1]
        # result = 1
        temp = 1
        dp2, dp3, dp5 = 0, 0, 0
        result = [1] * n
        while temp < n:
            result[temp] = min(result[dp2] * 2,
                               result[dp3] * 3,
                               result[dp5] * 5)
            # while result[dp2]*2 <= result[temp]:
            #     dp2 += 1
            # while result[dp3]*3 <= result[temp]:
            #     dp3 += 1
            # while result[dp5]*5 <= result[temp]:
            #     dp5 += 1
            if result[dp2] * 2 == result[temp]:
                dp2 += 1
            if result[dp3] * 3 == result[temp]:
                dp3 += 1
            if result[dp5] * 5 == result[temp]:
                dp5 += 1
            temp += 1
        return result[temp - 1]
