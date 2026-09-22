## --- Insertion and Deletion in CLL ---
# A Circular Linked List is a linked list where the last node points back to the first node instead of pointing to None.
# Here there is no None part at first or last node.
#
# Operations:
# 1. Insert at beginning
# 2. Insert at end
# 3. Insert at a given position
# 4. Delete first node
# 5. Delete last node
# 6. Delete node from a given position
# 7. Display the list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    ## Initially we don't have any next node connection so assign as None

class CLL:
    def __init__(self):
        self.head = None    ## Always initially we have to assign head node as None.

    # Insert at beginning
    def first(self, data):
        new = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        new.next = self.head
        temp.next = new
        self.head = new

    # Insert at end
    def last(self, data):
        NL = Node(data)
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new
        new.next = self.head

    # Insert at given position
    def middle(self, data, pos):
        NM = Node(data)
        if pos == 0:
            self.first(data)
            return

        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        NM.next = temp.next
        temp.next = NM

  
    # Delete first node
    def dl_first(self):
        if self.head is None:
            return
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = self.head.next
        self.head = self.head.next

    # Delete last node
    def dl_last(self):
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        temp.next = self.head

    # Delete node from given position
    def dl_mid(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.dl_first()
            return
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        temp.next = temp.next.next

    # Display Circular Linked List
    def display(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        while temp.next != self.head:
            print(temp.data, "-->", end=' ')
            temp = temp.next
        print(temp.data)

# Create Circular Linked List
c = CLL()
N1 = Node(11)
c.head = N1

N2 = Node(22)
N1.next = N2

N3 = Node(33)
N2.next = N3

N4 = Node(44)
N3.next = N4

N5 = Node(55)
N4.next = N5

N5.next = N1

# Operations
# d.first(5)
# d.last(66)
# d.middle(90, 2)

# d.dl_first()
# d.dl_last()
# d.dl_mid(3)

c.display()
