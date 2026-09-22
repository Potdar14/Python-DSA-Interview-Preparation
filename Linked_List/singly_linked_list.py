class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # Insert at last
    def last(self, data):
        NL = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = NL

    # Insert at middle / given position
    def middle(self, data, pos):
        NM = Node(data)
        if self.head is None:
            self.head = NM
            return
          
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        NM.next = temp.next
        temp.next = NM

  
    # Delete first node
    def delete(self):
        if self.head is None:
            print("Empty List")
            return
        self.head = self.head.next

    # Delete last node
    def dl_last(self):
        if self.head is None:
            print("Empty List")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete middle / given position
    def dl_mid(self, pos):
        if self.head is None:
            print("Empty List")
            return

        if pos <= 0:
            print("Invalid position")
            return

        if pos == 1:
            self.head = self.head.next
            return
          
        temp = self.head
        for i in range(pos - 1):
            temp = temp.next
        temp.next = temp.next.next

    # Display linked list
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head
            while temp:
                print(temp.data, "-->", end=" ")
                temp = temp.next
            print("None")

# Creating Linked List
s = SLL()
N1 = Node(11)
s.head = N1    ## assign first node as head

N2 = Node(22)
N1.next = N2

N3 = Node(33)
N2.next = N3

N4 = Node(44)
N3.next = N4

N5 = Node(55)
N4.next = N5

# to get output we will call that function we want..

# Display
s.display()

