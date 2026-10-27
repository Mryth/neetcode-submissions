class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, cur = [],[]

        def back_track(start):
            res.append(cur[:])
            for i in range(start, len(nums)):
                cur.append(nums[i])
                back_track(i+1)
                cur.pop()
        
        back_track(0)
        return res