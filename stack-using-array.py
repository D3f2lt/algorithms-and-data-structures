"""
Author: PyDev
Description: Stack is a list based data structure that have a bit of a different flair
             than Array and Linked List.Will be using an Array to implement a Stack.
"""

class Stack:
    """
    class Stack represent the building block for Stack objects

    Methods:
        - push
        - top
        - pop
        - isEmpty
    """
    def __init__(self):
        """
        Initilize Stack object instance

        Arguments:
            - array_list: default to empty List, represent a List
        """
        self.array_list = list()
        print type(self.array_list)

    def push(self, new_element):
        """
        Adds new element to collection

        Arguments:
            - new_element: An object to be added to the List
        """
        self.array_list.append(new_element)

    def top(self):
        """Returns most recently-added element"""
        if not self.isEmpty():
            return self.array_list[-1]
        else:
            print "Stack is empty!"

    def pop(self):
        """Remove and returns most recently added element"""
        return self.array_list.pop()

    def isEmpty(self):
        """Check if a Stack object is empty"""
        if not self.array_list:
            return True
        else:
            return False
