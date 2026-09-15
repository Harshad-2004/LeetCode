class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = 0  # Next valid starting index
        
        # Check every possible center (2*n - 1 centers)
        for center in range(2 * n - 1):
            l = center // 2
            r = l + (center % 2)
            
            # Expand center until length is at least k
            while l >= last_end and r < n and s[l] == s[r]:
                length = r - l + 1
                if length >= k:
                    # Found a minimal valid palindrome of length k or k + 1
                    ans += 1
                    last_end = r + 1
                    break
                l -= 1
                r += 1
                
        return ans