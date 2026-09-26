# Problem: Palindrome Linked List
#
# Given the head of a singly linked list, determine whether
# the linked list is a palindrome.
# A palindrome is a sequence that reads the same forward
# and backward.
#
# Example 1:
# Input:  1 -> 2 -> 3 -> 2 -> 1
# Output: True
#
# Example 2:
# Input:  1 -> 2 -> 3
# Output: False
#
# Explanation:
# Find the middle of the linked list using slow and fast
# pointers. Then reverse the second half and compare it
# with the first half.

# Note - In SLL there is no prev part but here while checking palindrome we take prev as normal variable for temporarily while reversing.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Reverse a Linked List
def reverse(head):
    prev = None   
    temp = head    ## to traverse the list we use temp

    while temp:
        next_node = temp.next
        temp.next = prev
        prev = temp
        temp = next_node
    return prev

# Check Palindrome
def is_palindrome(head):
    if head is None or head.next is None:
        return True

    # Find the middle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         ## moves 1 step
        fast = fast.next.next    ## moves 2 steps

    # Reverse the second half
    second_half = reverse(slow)   ## Reverse the linked list starting from the current node which points slow

    # Compare both halves
    first_half = head       

    while second_half:
        if first_half.data != second_half.data:
            return False
        first_half = first_half.next
        second_half = second_half.next
    return True

# Create Linked List
N1 = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(2)
N5 = Node(1)
N1.next = N2
N2.next = N3
N3.next = N4
N4.next = N5

# Check whether the Linked List is a palindrome
print("Is Palindrome:", is_palindrome(N1))


# Time Complexity: O(n)
# Space Complexity: O(1)
