from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        # min_len[i] = min length of a valid subarray ending at or before index i
        min_len = [float('inf')] * n
        
        left = 0
        curr_sum = 0
        ans = float('inf')
        best_so_far = float('inf')
        
        for right in range(n):
            curr_sum += arr[right]
            
            # Shrink window when sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            # Found a subarray summing to target
            if curr_sum == target:
                curr_len = right - left + 1
                
                # Pair with the best non-overlapping subarray before index left
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, curr_len + min_len[left - 1])
                    
                best_so_far = min(best_so_far, curr_len)
                
            min_len[right] = best_so_far
            
        return ans if ans != float('inf') else -1