class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        l = []
        for account in accounts:
            s = 0
            for num in account:
                s += num
            l.append(s)
        return max(l)

        