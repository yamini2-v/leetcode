class Solution:
    def isPalindrome(self, x: int) -> bool:
     temp = x
     r = 0
     while temp > 0:
        n = temp % 10
        r = r * 10 + n
        temp = temp // 10
     if r == x:
        return True
     else:
        return False


        
