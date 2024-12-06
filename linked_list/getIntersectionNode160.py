"""
https://leetcode.com/problems/intersection-of-two-linked-lists/description/

https://vimeo.com/900448479/5a9e916e52?share=copy
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pointerA = headA
        pointerB = headB

        while pointerA != pointerB:
            # If pointerA reaches the end of list A, start from the head of list B
            # If pointerB reaches the end of list B, start from the head of list A
            pointerA = pointerA.next if pointerA else headB
            pointerB = pointerB.next if pointerB else headA
        return pointerA
