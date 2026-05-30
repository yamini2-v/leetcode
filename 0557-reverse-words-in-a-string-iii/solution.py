class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        list1 = s.split()
        for x in list1:
            result.append(x[::-1])
        return ' '.join(result)

        
        
