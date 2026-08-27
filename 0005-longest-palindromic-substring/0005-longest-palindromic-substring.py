class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        start, max_len = 0, 0
        
        def expand_around_center(left, right):
            # Expand outwards as long as bounds are valid and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return length of valid palindrome
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindromes (single center character)
            len1 = expand_around_center(i, i)
            # Even length palindromes (center between i and i + 1)
            len2 = expand_around_center(i, i + 1)
            
            length = max(len1, len2)
            
            # Update starting index and max length if a longer palindrome is found
            if length > max_len:
                max_len = length
                start = i - (length - 1) // 2
                
        return s[start : start + max_len]