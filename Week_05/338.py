class Solution(object):

    def countBits(self, num):
        dp = [0]
        slot = 1
        for i in range(1, num + 1):
            dp.append(1 + dp[i - slot])
            if i == 2 * slot - 1:
                slot *= 2
        return dp
