"""
https://leetcode.com/problems/middle-of-the-linked-list/

https://vimeo.com/899346557/ffc03046a8?share=copy

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

eg 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

eg 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        # Find the middle node using the two-pointer approach
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Collect the nodes from the middle to the end
        result = []
        while slow is not None:
            result.append(slow.val)
            slow = slow.next

        return result


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Main Code to Test the Solution
if __name__ == "__main__":
    # Example 1
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    solution = Solution()
    output = solution.middleNode(head)
    print(f"Input: {values}")
    print(f"Output: {output}")

    # Example 2
    values = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(values)
    output = solution.middleNode(head)
    print(f"\nInput: {values}")
    print(f"Output: {output}")
