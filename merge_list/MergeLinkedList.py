'''
    @params first_list, second_list are linked list
    @return a new linked_list

'''
from .exceptions import RemovingFromEmptyLinkedList

def linked_list(first_link, second_link):
    new_linked_list = LinkedList()
    i = first_link.size + second_link.size
    while(i >= 1):
        if first_link.get_current() < second_link.get_current():
            try:
                old_value = first_link.get_current()
                first_link.move_up()
                new_linked_list.append(old_value)
            except StopIteration:
                try:
                    old_value = second_link.get_current()
                    second_link.move_up()
                    new_linked_list.append(old_value)
                except StopIteration:
                    raise ValueError()
        elif second_link.get_current() < first_link.get_current():
            try:
                old_value = second_link.get_current()
                second_link.move_up()
                new_linked_list.append(old_value)
            except StopIteration:
                try:
                    old_value = first_link.get_current()
                    first_link.move_up()
                    new_linked_list.append(old_value)
                except StopIteration:
                    raise ValueError("uh oh")
        i -= 1
    return new_linked_list
'''
    # linked list
    @constructor
        size of list
        header
        tail
        current
        linked_list
    @methods
        get_current(): @return
                            current list item
        __iter__():
        remove(): remove current element
        append(): add element to list

'''

class LinkedList:
    def __init__(self):
        self.size = 0
        self.header = Link(None, None)
        self.tail = self.header
        self.current = self.header
    def get_current(self):
        return self.current.get_next().element
    def get_tail(self):
        return self.tail.get_next()
    def append(self, element):
        appended = Link(element, None)
        #check if linked_list is empty
        if self.header.get_next().element == None:
            self.header.set_next(appended)
            #tail point to the previous link of the first link in the linked_list
            self.tail = appended
            self.size += 1
            return self
        self.tail.set_next(appended)
        self.tail = self.tail.get_next()
        self.size += 1
        return self
    def remove(self):
        removed = self.current.get_next()
        try:
            assert self.get_size() > 0
            if self.tail == removed:
                #change tail to current
                self.tail = self.current
            #set current element to None
            self.set_current_to_next()
            self.size -= 1     
        except AssertionError:
            raise RemovingFromEmptyLinkedList()
    def set_current_to_next(self):
        self.current.set_next(self.current.get_next().get_next())
        return
    def __iter__(self):
        return self
    def __next__(self):
        self.current = self.current.get_next()
        for i in range(self.get_size()):
            self.current = self.current.get_next()
            print(i)
            yield self.current.element
        #start at the beginning
        self.current = self.header
    def get_last(self):
        return self.tail
    def move_up(self):
        if self.size == 0:
            raise NotImplementedError()
        if self.tail == self.header:
            raise StopIteration()
        self.current = self.current.get_next()
    def get_size(self):
        return self.size


    

'''
    # Link
    @constructor
        element: value of link
        next: next elemenet
    @methods
        setNext(): set next element
        getPrev(): 
'''

class Link:
    def __init__(self, value, next):
        self.element = value
        self.next = next
        if next == None:
            self.next = self
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def __gt__(self, link):
        if self.element > link.element:
            return True
        return False
    def __ls__(self, link):
        if self.element < link.element:
            return True
        return False
    
if __name__ == "__main__":
    first_list = LinkedList()
    first_list.append(3).append(5).append(6)
    second_list = LinkedList()
    second_list.append(1).append(2).append(5)
    for element in linked_list(first_list, second_list):
        print(element)