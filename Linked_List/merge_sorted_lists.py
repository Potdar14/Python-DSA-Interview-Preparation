# Problem: Merge Two Sorted Linked Lists
# Given two sorted linked lists, merge them into one sorted
# linked list and return the head of the merged list.
#
# Example:
# List 1: 1 -> 3 -> 5
# List 2: 2 -> 4 -> 6
#
# Output:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
#
# Explanation:
# Compare the nodes of both lists and connect the smaller
# node to the merged list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(list1, list2):
    dummy = Node(0)
    current = dummy
  
    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Add remaining nodes
    if list1:
        current.next = list1
    else:
        current.next = list2
    return dummy.next

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Create first sorted linked list
N1 = Node(1)
N2 = Node(3)
N3 = Node(5)
N1.next = N2
N2.next = N3

# Create second sorted linked list
M1 = Node(2)
M2 = Node(4)
M3 = Node(6)
M1.next = M2
M2.next = M3

# Merge two sorted lists
merged_head = merge_lists(N1, M1)
display(merged_head)

# Time Complexity: O(n + m)
# Space Complexity: O(1)
