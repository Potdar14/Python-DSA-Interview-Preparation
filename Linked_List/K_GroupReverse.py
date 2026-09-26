# Problem: Reverse Nodes in k-Group
# Given a singly linked list, reverse the nodes
# in groups of k.
#
# Example:
# Input:
# 1 -> 2 -> 3 -> 4 -> 5
# k = 2
#
# Output:
# 2 -> 1 -> 4 -> 3 -> 5


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_k_group(head, k):
    temp = head
    count = 0
    while temp and count < k:
        temp = temp.next
        count += 1

    # Less than k nodes remain
    if count < k:
        return head
    # Reverse k nodes
    prev = None
    temp = head
    count = 0
    while temp and count < k:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
        count += 1

    # head is now the last node of reversed group
    head.next = reverse_k_group(temp, k)
    return prev

def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Create Linked List
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N5 = Node(5)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

# Reverse nodes in groups of 2
head = reverse_k_group(N1, 2)
display(head)


# Time Complexity: O(n)
# Space Complexity: O(n) because of recursion
