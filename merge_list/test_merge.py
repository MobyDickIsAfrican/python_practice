from logging import exception
import unittest
from .MergeLinkedList import LinkedList
from .exceptions import RemovingFromEmptyLinkedList

class MergeListTest(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()
    def test_appended_is_tail(self):
        self.linked_list.append(5)
        print("whoa")
        self.assertEqual(self.linked_list.tail.element, 5)
    def test_size_when_appended(self):
        self.linked_list.append(5)
        self.assertEqual(self.linked_list.size, 1)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.size, 2)
    def test_element_appended(self):
        self.linked_list.append(5)
        self.linked_list.append(3)
        self.assertEqual(self.linked_list.current.get_next().element, 5)
        self.assertEqual(self.linked_list.current.get_next().get_next().element, 3)
        

class RemoveTest(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
    def test_remove_current_from_empty_list(self):
        self.assertRaises(RemovingFromEmptyLinkedList, lambda: self.list.remove())
    def test_remove_last_link(self):
        self.list.append(5).append(7).append(3)
        self.list.move_up()
        self.list.remove()
        self.assertEquals(self.list.get_tail().element, 3)
        self.assertEquals(self.list.get_size(), 2)

class IterationTest(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()
    #filo refers to first in last out
    def test_filo_list_correct(self):
        self.list.append(1).append(2).append(3)
        for item in self.list:
            print(item)
