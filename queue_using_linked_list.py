"""
Author: PyDev
Description: Implementing Queue using Doubly-Linked List with a Tail
"""

from doubly_linked_list_with_tail import DoublyLinkedListWithTail, Element

class Queue:
    def __init__(self):
        """Initialize Queue instance"""
        self.linked_list = DoublyLinkedListWithTail()

    def enqueue(self, new_element):
        """Add new_element to the back of the Linked List"""
        self.new_element = Element(new_element)
        self.linked_list.pushBack(self.new_element)

    def dequeue(self):
        """Remove and return least recently added element"""
        element = self.linked_list.topFront()
        self.linked_list.popFront()
        return element.value

    def isEmpty(self):
        """Return a Boolean value after checking if the Queue is empty or not"""
        return self.linked_list.isEmpty()
