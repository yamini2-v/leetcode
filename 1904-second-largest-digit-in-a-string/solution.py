class Solution:
    def secondHighest(self, s: str) -> int:
        l = set()
        for i in s:
            if i.isdigit():
                l.add(int(i))        
        k = sorted(list(l))
        if len(l)> 1:
            return k[-2]
        else:
            return -1
        
