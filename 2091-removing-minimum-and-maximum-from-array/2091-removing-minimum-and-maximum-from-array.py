class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
            
        # Find 0-based indices of min and max elements
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        # Determine relative positions
        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)
        
        # Calculate costs for all 3 removal strategies
        both_front = right + 1
        both_back = n - left
        from_both_ends = (left + 1) + (n - right)
        
        return min(both_front, both_back, from_both_ends)