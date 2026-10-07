class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low,high+1):
            if len(str(i)) % 2 == 0:
                s = str(i)
                l = len(s)//2
                p = s[:l]
                q = s[l:]
                u = sum(int(x) for x in p)
                v = sum(int(y) for y in q)
                if u == v:
                    count += 1
        return count

        