"""
https://leetcode.com/problems/linked-list-cycle/

https://vimeo.com/899346557/ffc03046a8?share=copy

eg 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

eg 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

eg 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# Helper function to create a linked list with or without a cycle
def create_linked_list(values, cycle_pos=-1):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    nodes = [head]  # Store nodes to create a cycle later if needed

    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
        nodes.append(current)

    # Create a cycle if cycle_pos is valid
    if cycle_pos >= 0:
        current.next = nodes[cycle_pos]

    return head


# Main code to test the Solution
if __name__ == "__main__":
    # Example 1: List with a cycle
    values = [3, 2, 0, -4]
    cycle_pos = 1  # Position where the cycle starts
    head = create_linked_list(values, cycle_pos)
    solution = Solution()
    print(f"Cycle in Linked List: {solution.hasCycle(head)}")  # Expected: True

    # Example 2: List without a cycle
    values = [1, 2, 3, 4]
    cycle_pos = -1  # No cycle
    head = create_linked_list(values, cycle_pos)
    print(f"Cycle in Linked List: {solution.hasCycle(head)}")  # Expected: False

"""
Time complexity: O(n)
Space complexity: O(1)
"""