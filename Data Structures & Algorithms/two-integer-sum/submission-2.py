class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        T = target
        seen = {}
        for i, x in enumerate(nums):
            if T-x in seen:return [seen[T-x],i]
            else:
                seen[x] = i
        return [-1,-1]