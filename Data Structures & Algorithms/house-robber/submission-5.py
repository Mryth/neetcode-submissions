class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = dict()

        def gain(i):
            if i < 0:return 0
            if i == 0 or i == 1:memo[i] = nums[i]
            if i == 2:memo[i] = nums[2] + gain(0)
            elif i not in memo:
                memo[i] = max(gain(i-2)+nums[i], gain(i-3)+nums[i])
            return memo[i]
        
        return max(gain(n-1),gain(n-2))