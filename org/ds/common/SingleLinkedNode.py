class SingleLinkedNode:
    def __init__(self, data):
        self.next = None;
        self.data = data;

    def __str__(self):
        return "SinglyLinkedNode is " + self.data;