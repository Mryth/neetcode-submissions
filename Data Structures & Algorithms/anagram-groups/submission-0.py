class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:return []
        hash_map = dict()
        results = []

        for s in strs:
            key = "".join(sorted(s))
            if key in hash_map:
                results[hash_map[key]].append(s)
            else:
                hash_map[key] = len(results)
                results.append([s])
        return results