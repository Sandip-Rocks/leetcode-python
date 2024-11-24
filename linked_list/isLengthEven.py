"""
https://www.geeksforgeeks.org/problems/linked-list-length-even-or-odd/1

Given a linked list, your task is to complete the function isLengthEven() which contains the head of the linked list,
and check whether the length of the linked list is even or not.
Return true if it is even, otherwise false.

eg:
Input: Linked list: 12->52->10->47->95->0
Output: true
Explanation: The length of the linked list is 6 which is even, hence returned true.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Helper to append nodes to the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")


class Solution:
    def isLengthEven(self, head):
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        return length % 2 == 0


# Main Code to Execute
if __name__ == "__main__":
    # Create a linked list
    ll = LinkedList()
    data = [12, 52, 10, 47, 95, 0]  # Input data for the linked list
    for value in data:
        ll.append(value)

    print("Linked List:")
    ll.display()

    # Create Solution object and check if the length is even
    sol = Solution()
    result = sol.isLengthEven(ll.head)

    print("\nIs the length of the linked list even?:", result)
  
"""
Time complexity: O(n)
Space complexity: O(1)
"""