"""
https://leetcode.com/problems/linked-list-cycle-ii/description/

https://vimeo.com/899963238/abea9108b6?share=copy



"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        while head is not slow:
            head = head.next
            slow = slow.next
        return slow