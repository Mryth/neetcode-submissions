class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        l,r = 0,len(s1)-1
        tools = Counter(s1)
        while r < len(s2):
            if tools == Counter(s2[l:r+1]):return True
            l+=1
            r+=1
        return False