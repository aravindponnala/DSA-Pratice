class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


"""

In double LL we have two types of Inseration
a--> Front Traversal
b--> Back Traversal

"""


class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.n = 0

    def insertion_at_front(self, value):
        new_node = Node(value)

        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.pre = new_node

        self.head = new_node
        self.n += 1


    def insertion_at_back(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = None
        new_node.prev = current_node


    def print_double_ll_from_front(self):
        curr = self.head
        result = ""
        while curr is not None:
            print(curr)
            result = result + "--->"+str(curr.data)
            curr = curr.next

        result += "--->None"
        return result
    
    def print_double_ll_from_back(self):
        current_node = self.head
        result = ""
        """first we need to reach the last now to get from back"""
        while current_node.next is not None:
            print(current_node.data)
            current_node = current_node.next

        while current_node is not None:
            #  print(current_node.data)
             result += str(current_node.data) + " <--- "
             current_node = current_node.prev

        result += "None<---"
        return result


dll = Double_Linked_List()
dll.insertion_at_front(5)
dll.insertion_at_front(6)
dll.insertion_at_front(7)


dll.insertion_at_back(10)
dll.insertion_at_back(20)
dll.insertion_at_back(30)

print(dll.print_double_ll_from_front())

print(dll.print_double_ll_from_back())
