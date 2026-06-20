class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for i in range(len(jewels)):
            c = 0
            c = stones.count(jewels[i])
            sum += c
        return sum
        
