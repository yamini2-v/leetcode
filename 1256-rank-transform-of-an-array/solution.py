class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l = []
        s = sorted(set(arr))
        d = {}
        for i in range(len(s)):
            d[s[i]] = i+1
        for i in arr:
            l.append(d[i])
        return l

        
