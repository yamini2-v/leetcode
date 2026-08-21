class Solution:
    def addDigits(self, num: int) -> int:
        def add(num):
            s = 0
            while num > 0:
                d = num%10
                s += d
                num = num//10
            return s

        while num >= 10:
            num = add(num)
        return num
            

        
            

        
