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
            """hear we go until last node next value is none but not until last node it means we stop at node where
            we get the last node address"""
            """ Instead of while current_node != None, we use while current_node.next != None so that current_node 
            is still valid when inserting."""
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
            """
            current_node == None
            Used to determine if you have reached the end of a traversal or if the list is empty.
            Use current_node == None when you are iterating through a list and need to check if you've completely run out of nodes

            current_node.next == None
            This is used to determine if current_node is the last node in the list
            Use current_node.next == None when you need to stop at the last node
            (e.g., when appending or deleting elements) to avoid accessing None.next, which would cause an error.
            """
            if current_node.data == after_value:
                new_node.next = current_node.next
                current_node.next = new_node
                self.n = self.n + 1
                return
            current_node = current_node.next

        print(f"{after_value}" + "-not founded in Linked List")
        """ hera we can use return stmnt like return f"{after_value}" + "-not founded in Linked List") 
        but if we use return we need to use print while creating object like print(l.after_insert(4, 90))"""

    def empty_linked_list(self):
        """just make head as none automatically we will lost connect to very node so it wiil be empty"""
        self.head = None
        self.n = 0

    def delete_item_at_head(self):
        """to delete first item in linked list we need to just make next value as head"""
        if self.head == None:
            print("List is empty")
            return
        self.head = self.head.next
        self.n = self.n - 1

    def delete_item_at_last(self):
        if self.head == None:
            print("List is empty")
            return

        if self.head.next == None:
            print("List only have one item")
            """ delete last item  means we need to make linked list as empty"""
            """ **** is there any differenec between deleting head or emptying 
            the list if there only one item in linked list when we want to pop item from lnked list  
            ---- the result is same so no worries"""
            self.empty_linked_list()
            return

        current_node = self.head
        while current_node.next.next != None:
            current_node = current_node.next
        current_node.next = None
        self.n = self.n - 1

    def remove(self, delete_value):
        if self.head is None:
            print("List is empty")
            return

        # Check if the head itself needs to be deleted
        if self.head.data == delete_value:
            print(f"Deleting head node with value {delete_value}")
            self.head = self.head.next
            return

        current_node = self.head
        while current_node and current_node.next:
            if current_node.next.data == delete_value:
                print(f"Deleting node with value {delete_value}")
                current_node.next = current_node.next.next
                return  # Exit after deletion

            current_node = current_node.next

        print(f"Value {delete_value} not found in the list.")

    def search_by_index(self, index_value):
        if index_value < 0:
            print("Index cannot be negative.")
            return None

        current_node = self.head
        pos = 0

        while current_node:
            if pos == index_value:
                print(current_node.data, "---")  # Print the found item
                return current_node.data

            current_node = current_node.next
            pos += 1

        print(f"Index {index_value} is out of range.")  # Handle out of range
        return None


l = LinkedList()
l.insert_at_head(1)
l.insert_at_head(2)
l.insert_at_head(3)
l.insert_at_tail(4)
l.insert_at_tail(5)
l.after_insert(4, 90)
l.after_insert(9, 100)

print(l, "after_insert")
# l.delete_item_at_head()
# print(l, "delete_item_at_head")
# l.delete_item_at_last()
# print(l, "delete_item_at_last")
# l.empty_linked_list()
# print(l, "empty_linked_list")
l.remove(90)
l.remove(5)
l.remove(4)
l.remove(3)
print(l, "after remove")

print(l.search_by_index(1), "search_by_index")
