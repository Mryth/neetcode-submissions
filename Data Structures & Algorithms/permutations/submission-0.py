class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def back_track(current):
            if len(current) == len(nums):
                results.append(current[:])
                return
            for n in set(nums)-set(current):
                current.append(n)
                back_track(current)
                current.pop()

        back_track([])
        return results