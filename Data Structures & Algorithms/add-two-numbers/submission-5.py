# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        running = dummy
        dummy.next = running
        carry = 0
        while l1 and l2:
            sum_val = l1.val + l2.val + carry
            running.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            running = running.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            sum_val = l1.val + carry
            running.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            running = running.next  # Must advance running
            l1 = l1.next
            
        # 4. Process remaining l2 nodes (whether carry is present or not)
        while l2:
            sum_val = l2.val + carry
            running.next = ListNode(sum_val % 10)
            carry = sum_val // 10
            running = running.next  # Must advance running
            l2 = l2.next
        if carry > 0:
            running.next = ListNode(carry)

        return dummy.next