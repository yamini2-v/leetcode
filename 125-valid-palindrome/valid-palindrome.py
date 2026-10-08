class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = []
        for ch in s:
            if ch.isalnum():
                l.append(ch.lower())
        return l == list(reversed(l))

        