class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = dict()
        def cost_opt(i):
            if i == 0:
                memo[0] = cost[0]
            if i == 1:
                memo[1] = cost[1]
            elif i not in memo:
                memo[i] = min(cost_opt(i-1)+cost[i],cost_opt(i-2)+cost[i])
            return memo[i]
            
        return min(cost_opt(n-1), cost_opt(n-2))