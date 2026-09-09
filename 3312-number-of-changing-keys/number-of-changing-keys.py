class Solution:
    def countKeyChanges(self, s: str) -> int:
        n = len(s)
        q = s.lower()
        c = 0
        for i in range(1,n):
            if q[i] != q[i-1]:
                c += 1
        return c
        