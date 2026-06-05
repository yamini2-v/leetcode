class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict()
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for (k,v) in d.items():
            if v == 1:
                return s.index(k)
        return -1

        
