class Solution:
    def climbStairs(self, n: int) -> int:
        # two approaches bottum - up  up down
        # we try up down
        # bottom up and up down ! one of the two approaches.

        memo = {}
        def f(k):
            if k == n:
                return 1
            if k > n:
                return 0
            if k in memo:
                return memo[k]
            memo[k] = f(k+1) + f(k+2)
            return memo[k]
        return f(0)