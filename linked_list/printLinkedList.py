"""
https://www.geeksforgeeks.org/problems/print-linked-list-elements/1
"""
#Your task is to complete this function
#Your function should print the data in one line only

'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    # Function to display the elements of a linked list
    def display(self, head):
        #code here
        while head:
            print(head.data, end = ' ') # print the data in same line
            head = head.next

