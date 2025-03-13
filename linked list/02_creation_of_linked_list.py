class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    # hear we have created empty list
    def __init__(self):
        self.head = None  # as first node always called as head if we want to create empty node we need to  make head as None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_at_head(self, value):
        # create new node
        new_node = Node(value)
        # create connection
        # print(self.head, "-----")
        new_node.next = self.head
        self.head = new_node
        # print(self.head.data, "--")
        self.n = self.n + 1

    def __str__(self):
        result = ""
        curr = self.head
        while curr != None:
            result = result + f"{curr.data}" + "-->"
            curr = curr.next
        return result

    def insert_at_tail(self, value):
        new_node = Node(value)

        if self.head == None:
            """If self.head is None, it sets new_node as the head."""
            self.head = new_node
            return
        current_node = self.head

        while current_node.next is not None:
            """hear we go until last node next value is none but not until last node it means we stop at node where we get the last node address"""
            """ Instead of while current_node != None, we use while current_node.next != None so that current_node is still valid when inserting."""
            current_node = current_node.next
        current_node.next = new_node
        self.n = self.n + 1

    def after_insert(self, after_value, value):
        if self.head == None:
            print("List is empty")
            return

        new_node = Node(value)
        current_node = self.head
        while current_node:
            if current_node.data == after_value:
                new_node.next = current_node.next
                current_node.next = new_node
                self.n = self.n + 1
                return
            current_node = current_node.next

        print(f"{after_value}" + "-not founded in Linked List")
        """ hera we can use return stmnt like return f"{after_value}" + "-not founded in Linked List") 
        but if we use return we need to use print while creating object like print(l.after_insert(4, 90))"""


l = LinkedList()
l.insert_at_head(1)
l.insert_at_head(2)
l.insert_at_head(3)
l.insert_at_tail(4)
l.insert_at_tail(5)
l.after_insert(4, 90)
l.after_insert(9, 100)
print(l)
