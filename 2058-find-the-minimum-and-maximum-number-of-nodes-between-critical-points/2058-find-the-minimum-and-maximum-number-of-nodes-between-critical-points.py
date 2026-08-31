# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        prev = head
        curr = head.next
        index = 1  # 0-indexed position of curr node
        
        first_critical = -1
        prev_critical = -1
        min_dist = float('inf')
        
        while curr.next:
            nxt = curr.next
            
            # Check if current node is a local maxima or minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_critical == -1:
                    first_critical = index
                else:
                    min_dist = min(min_dist, index - prev_critical)
                
                prev_critical = index
            
            prev = curr
            curr = nxt
            index += 1
            
        if first_critical == -1 or first_critical == prev_critical:
            return [-1, -1]
        
        max_dist = prev_critical - first_critical
        return [min_dist, max_dist]