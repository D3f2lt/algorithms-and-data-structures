"""
Author: PyDev
Description: Doubly Linked List with a Tail consist of a element, where the element is the
             skeleton and consist of a value next, and previous variable/element.
             There is a Head pointer to refer to the front of the Linked List.
             The Tail pointer to refer to the end of Linked List/last elment
"""

class Element:
    """ A class that represent single skeleton of the Linked List"""
    def __init__(self, value):
        """
        initiliaze new elements of the linked list with new value

        Arguments:
            - value: any object reference to assign new element to Linked List

        Instance varabiles:
            - value: an object value
            - next: a reference/pointer to next element in the linked list and default value is None
            - previous: a reference/pointer to previous element in the linked list and default value is None
        """
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedListWithTail:
    """
    A class of Doubly-Linked List where it have attributes and properties, such as:
        - Doubly Linked List
        - With tail
    Methods:
        - pushFront(new_element)
        - topFront()
        - popFront()
        - pushBack(new_element)
        - topBack()
        - popBack()
        - find()
        - erase()
        - isEmpty()
        - addBefore()
        - addAfter()
    """
    def __init__(self, head = None):
        """
        initilize DoublyLinkedListWithoutTail object instance

        Arguments:
            - head: default to None

        Instance variables:
            - head: an object value which refer to head/start of the Linked List
            - Tail: an object value which refer to the back/end of the Linked List
        """
        self.head = self.tail = head

    def pushFront(self, new_element):
        """
        add new element to the front

        Arguments:
            - new_element: an object that reference to new element to be added
        """
        if self.tail:
            new_element.next = self.head
            self.head = new_element
            new_element.next.previous = self.head
        else:
            self.head = self.tail = new_element

    def topFront(self):
        """
        return front element/item

        Returns:
            - the front element/item object
        """
        return self.head

    def popFront(self):
        """remove front element/item"""
        if self.head:
            next_element = self.head.next
            if next_element:
                next_element.previous = None
            else:
                self.tail = None
            previous_head_object = self.head
            self.head = next_element
        else:
            print("Doubly Linked List With Tail is empty!")

    def pushBack(self, new_element):
        """
        add to back,also known as append

        Arguments:
            - new_element: an object that reference to new element to be added
        """
        if self.tail:
            self.tail.next = new_element
            new_element.previous = self.tail
            self.tail = new_element
            
        else:
            self.head = self.tail = new_element
            new_element.previous = None

    def topBack(self):
        """
        return back/last element/item

        Returns:
            - the back/last element/item object
        """
        if self.tail:
            return self.tail
        else:
            print("Doubly Linked List With Tail is empty!")

    def popBack(self):
        """
        remove back element/item
        """
        if self.head:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.tail = self.tail.previous
                self.tail.next = None
        else:
            print("Error! Doubly Linked List With Tail is empty!")

    def find(self, value):
        """
        find if the value of an object is available in the current Linked List

        Arguments:
            - value: an object that represent a value we want to look for

        Returns:
            - boolean object
        """
        current = self.head
        if self.head:
            while current.value != value and current.next:
                current = current.next
            if current.value == value:
                return True
            else:
                return False
        else:
            print("Doubly Linked List Without Tail is empty!")

    def erase(self, value):
        """
        remove an element/item from Linked List

        Arguments:
            - value: an object that represent a value we want to look for
        """
        current = self.head
        while current.value != value and current.next:
            current = current.next
        if current.value == value:
            if self.head.value == value:
                # We can use self.popFront() or
                self.head = current.next
                current.next = None
            elif not current.next:
                # We can use self.popBack() or
                self.tail = current.previous
                current.previous = None
            else:
                next_element = current.next
                previous_element = current.previous

                previous_element.next = next_element
                next_element.previous = previous_element

                current.next = current.previous = None

    def isEmpty(self):
        """
        check if the Linked List is empty or not

        Reutruns:
            - boolean object
        """
        if self.head:
            return False
        else:
            return True

    def addBefore(self, new_element, node):
        """
        add new element/item before a position in the Linked List

        Arguments:
            - new_element: an object that reference to a new element to be added
            - node: an object that reference to an integer object that tells the
                        method to where place the new element/item
        """
        new_element.next = node
        new_element.previous = node.previous
        node.previous = new_element
        if new_element.previous:
            new_element.previous.next = new_element
        if self.head == node:
            self.head = new_element

    def addAfter(self, new_element, node):
        """
        add new element/item after a node/element/item in the Linked List

        Arguments:
            - new_element: an object that reference to a new element to be added
            - node: an object that is part of the Linked List elements
        """
        new_element.next = node.next
        new_element.previous = node
        node.next = new_element
        if new_element.next:
            new_element.next.previous = new_element
        if self.tail == node:
            self.tail = new_element
