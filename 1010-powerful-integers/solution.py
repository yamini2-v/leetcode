class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        l = set()
        for i in range(21):   # safe upper bound
            for j in range(21):
                z = (x**i) + (y**j)
                if z <= bound:
                    l.add(z)
                if y == 1:   # stop inner loop if y == 1
                    break
            if x == 1:       # stop outer loop if x == 1
                break
        return list(l)

        
