"""Creation of single node"""


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


n = Node(1) #it created the one single node

print(n.data)
print(n.next)
