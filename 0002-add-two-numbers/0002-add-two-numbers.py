class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values from the current nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Add the two digits and carry
            total = val1 + val2 + carry

            # Calculate digit and carry
            digit = total % 10
            carry = total // 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next