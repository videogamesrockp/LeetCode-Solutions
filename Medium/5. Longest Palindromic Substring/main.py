class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=s[0]
        for i in range(len(s)):
            for j in range(i, len(s) + 1):
                text = s[i:j]
                if text == text[::-1] and len(ans) < len(text):
                    ans = text
        return(ans)
