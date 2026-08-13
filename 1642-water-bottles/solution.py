class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c = numBottles
        while numBottles >= numExchange:
            d = numBottles // numExchange
            m = numBottles % numExchange
            c += d
            numBottles = d + m
        return c

        
