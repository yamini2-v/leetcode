class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count = 0
        for i in nums:
            s = str(i)
            for j in range(len(s)):
                if s[j] == str(digit):
                    count+= 1
        return count


        