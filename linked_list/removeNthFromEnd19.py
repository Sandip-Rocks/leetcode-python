"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

https://vimeo.com/899963238/abea9108b6?share=copy


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)  # Create a dummy node pointing to the head
        dummy.next = head
        fast = dummy
        slow = dummy

        # Move fast pointer n+1 steps ahead to create a gap of n nodes
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next


# Helper function to build a linked list from a list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list (for easy output)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test the function
values = [1, 2, 3, 4, 5]
n = 2
head = build_linked_list(values)

solution = Solution()
new_head = solution.removeNthFromEnd(head, n)

# Print the updated linked list as a list
print(linked_list_to_list(new_head))
