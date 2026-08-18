from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        
        # Case 1: k == n
        if k == n:
            return max(nums)
        
        # Case 2: k == 1
        if k == 1:
            counts = Counter(nums)
            valid = [x for x, count in counts.items() if count == 1]
            return max(valid) if valid else -1
        
        # Case 3: 1 < k < n
        counts = Counter(nums)
        ans = -1
        
        # First element is valid only if it appears exactly once in the entire array
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
            
        # Last element is valid only if it appears exactly once in the entire array
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans