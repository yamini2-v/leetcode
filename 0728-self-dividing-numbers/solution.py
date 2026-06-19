class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left,right+1):
            s = [int(x) for x in  str(i)]
            if all( j != 0 and i%j == 0  for j in s):
              l.append(i)
        return(l)

        
