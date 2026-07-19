class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for e in nums:
            if e not in d:
                d[e] = nums.count(e)
        sorted_data = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_data.keys())[:k]