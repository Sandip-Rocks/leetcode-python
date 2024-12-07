"""
https://leetcode.com/problems/merge-two-sorted-lists/

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to simplify logic
        temp = dummy  # Pointer for the merged list

        # Compare nodes from list1 and list2
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        # Append remaining nodes (at most one of these will execute)
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2

        return dummy.next  # Return the merged list starting from the first node
