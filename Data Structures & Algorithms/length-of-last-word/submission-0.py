class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s[::-1]
        ans = s.split()
        return len(ans[0])
