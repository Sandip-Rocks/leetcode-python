"""
Operations
1. Append: Add a new node at the end.
2. Prepend: Add a new node at the beginning.
3. Insert After: Insert a node after a specific node.
4. Delete: Delete a node by value.
5. Search: Check if a value exists in the list.
6. Reverse: Reverse the order of nodes.
7. Display: Print the linked list.
"""
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    # Add a new node at the end of the list
    def append(self, data):
        new_node = self.Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        current = self.head
        while current.next:  # Traverse to the end of the list
            current = current.next
        current.next = new_node

    # Add a new node at the beginning of the list
    def prepend(self, data):
        new_node = self.Node(data)
        new_node.next = self.head  # Link the new node to the current head
        self.head = new_node

    # Insert a node after a given node
    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print(f"Node with data {prev_data} not found.")
            return
        new_node = self.Node(data)
        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete(self, data):
        if not self.head:  # If the list is empty
            print("List is empty.")
            return

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if not current.next:
            print(f"Node with data {data} not found.")
            return

        # Unlink the node from the list
        current.next = current.next.next

    # Search for a node by value
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("null")

# Create a linked list
ll = LinkedList()

# Append elements
ll.append(10)
ll.append(20)
ll.append(30)

# Display the list
print("After append operations:")
ll.display()  # Output: 10 -> 20 -> 30 -> null

# Prepend an element
ll.prepend(5)
print("After prepend operation:")
ll.display()  # Output: 5 -> 10 -> 20 -> 30 -> null

# Insert after a specific node
ll.insert_after(10, 15)
print("After inserting 15 after 10:")
ll.display()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> null

# Delete a node
ll.delete(20)
print("After deleting 20:")
ll.display()  # Output: 5 -> 10 -> 15 -> 30 -> null

# Search for a value
print("Searching for 15:", ll.search(15))  # Output: True
print("Searching for 50:", ll.search(50))  # Output: False

# Reverse the list
ll.reverse()
print("After reversing the list:")

ll.display()  # Output: 30 -> 15 -> 10 -> 5 -> null
