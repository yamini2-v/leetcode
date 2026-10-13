class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squareSum = 0
        digitSum = 0
        while n > 0:
            d = n % 10 
            digitSum += d
            squareSum += d**2
            n = n//10
        return squareSum - digitSum >= 50



        
        