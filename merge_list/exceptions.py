
class RemovingFromEmptyLinkedList(Exception):
    def __init__(self):
        self.message = "Cant Remove Element From Empty Linked List"
        super().__init__(self.message)