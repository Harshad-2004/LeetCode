from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        # Count available characters in s
        count = Counter(s)
        
        # Step 1: Match target characters from left to right as far as possible
        matched_len = 0
        while matched_len < n and count[target[matched_len]] > 0:
            count[target[matched_len]] -= 1
            matched_len += 1
            
        # Step 2: Work backwards to find where we can make a character bigger
        for k in range(matched_len, -1, -1):
            if k < n:
                # Try finding a letter bigger than target[k]
                for char_code in range(ord(target[k]) + 1, ord('z') + 1):
                    ch = chr(char_code)
                    if count[ch] > 0:
                        # Pick this larger character
                        count[ch] -= 1
                        
                        # Build result: matched prefix + larger char + remaining chars sorted
                        prefix = target[:k]
                        tail = "".join(sorted(count.elements()))
                        return prefix + ch + tail
            
            # If no larger character was available, put target[k-1] back into available pool
            if k > 0:
                count[target[k - 1]] += 1
                
        return ""