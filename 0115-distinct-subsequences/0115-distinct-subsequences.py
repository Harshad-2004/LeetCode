class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        
        # If t is longer than s, t cannot be a subsequence of s
        if n > m:
            return 0
        
        # dp[j] stores the number of subsequences of s that equal t[:j]
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string t[:0] is always formed exactly 1 way
        
        for char_s in s:
            # Traverse backwards so dp[j - 1] represents the state from the previous character of s
            for j in range(n, 0, -1):
                if char_s == t[j - 1]:
                    dp[j] += dp[j - 1]
                    
        return dp[n]        