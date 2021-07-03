
class Stack:
    def __init__(self):
        self.top = 0
        self._array = []
        return self
    def push(self, element):
        self._array.append(element)
        self.top += 1
        return self
    def pop(self):
        popped_entry = self.top
        self.top -= 1
        self._array.pop()
        return popped_entry
    def get_size(self):
        return self.top
    def get_top(self):
        return self._array[-1]


print("hey")