class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    # Front
    def front(self):
        if self.head is not None:
            return self.head.data
        return None

    # Remove Front
    def removeFront(self):
        if self.head is not None:
            removed_data = self.head.data
            self.head = self.head.next
            return removed_data
        return None

    # Add Front
    def addFront(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Bonus: Add to Back
    def addToBack(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

# Example usage:
sll = SLL()
sll.addFront(3)
sll.addFront(2)
sll.addFront(1)

print("Front:", sll.front())  # Output: 1
print("Remove Front:", sll.removeFront())  # Output: 1
print("New Front:", sll.front())  # Output: 2

sll.addToBack(4)
sll.addToBack(5)

current = sll.head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 3 -> 4 -> 5 ->
