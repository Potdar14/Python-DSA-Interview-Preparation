### --- DLL Practice ---

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def first(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return

        temp = self.head

        new.next = temp       # forward connection
        temp.prev = new       # backward connection
        self.head = new

    # Insert at last
    def last(self, data):
        lst = Node(data)

        if self.head is None:
            self.head = lst
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = lst       # forward connection
        lst.prev = temp       # backward connection

    # Insert at middle / given position
    def middle(self, data, pos):
        NM = Node(data)

        if self.head is None:
            self.head = NM
            return

        if pos <= 1:
            self.first(data)
            return

        temp = self.head

        for i in range(pos - 1):
            if temp.next is None:
                break
            temp = temp.next

        NM.next = temp.next
        NM.prev = temp

        if temp.next is not None:
            temp.next.prev = NM

        temp.next = NM

    # Delete first node
    def dl_first(self):
        if self.head is None:
            print("Empty List")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

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

        if pos <= 1:
            self.dl_first()
            return

        temp = self.head

        for i in range(pos - 1):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next       # forward connection

        if temp.next is not None:
            temp.next.prev = temp        # backward connection

    # Display linked list
    def display(self):
        if self.head is None:
            print("Empty List")
        else:
            temp = self.head

            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next

            print("None")


# Creating Doubly Linked List
d = DLL()

N1 = Node(11)
d.head = N1

N2 = Node(22)
N1.next = N2
N2.prev = N1

N3 = Node(33)
N2.next = N3
N3.prev = N2

N4 = Node(44)
N3.next = N4
N4.prev = N3

N5 = Node(55)
N4.next = N5
N5.prev = N4


# Operations
# d.first(5)
# d.last(66)
# d.middle(90, 2)

# d.dl_first()
# d.dl_last()
# d.dl_mid(3)

d.display()
