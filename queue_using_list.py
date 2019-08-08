"""
Author: PyDev
Description: Implementing Queue Data Sturctures using List
"""

class Queue:
    """
        Queue module that contians the API required 
    """
    def __init__(self):
        """Initialize the Queue instance with an empty List"""
        self.list_elements = list()

    def enqueue(self, new_element):
        """Add new_element to the fist index of the List and shit the rest to the right"""
        self.list_elements.insert(0, new_element)

    def dequeue(self):
        """Remove and return least recently added element"""
        return self.list_elements.pop()

    def isEmpty(self):
        """Return a Boolean value after checking if the Queue is empty or not"""
        return self.list_elements == []

    def size(self):
        """Return an integer value representing the size of the Queue"""
        return len(self.list_elements)

    def __str__(self):
        """Used for testing"""
        result = ""
        for index, value in enumerate(self.list_elements):
            result += "\nindex = {}, value = {}".format(index, value)
        return result
