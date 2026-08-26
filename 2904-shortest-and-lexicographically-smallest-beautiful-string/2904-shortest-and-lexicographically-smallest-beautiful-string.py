class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones = [i for i, char in enumerate(s) if char == '1']
        
        if len(ones) < k:
            return ""
        
        ans = ""
        min_len = float('inf')
        
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]
            sub = s[start : end + 1]
            length = len(sub)
            
            if length < min_len:
                min_len = length
                ans = sub
            elif length == min_len:
                ans = min(ans, sub)
                
        return ans