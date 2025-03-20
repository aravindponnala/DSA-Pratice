class Node:
    def __init__(self, value):
        """
        Each node in a Doubly Linked List contains the data it holds, a pointer to the next node in the list,
        and a pointer to the previous node in the list. By linking these nodes together through the next and
        prev pointers, we can traverse the list in both directions (forward and backward), which is a key feature of a Doubly Linked List

        """
        self.data = value
        self.prev = None
        self.next = None
