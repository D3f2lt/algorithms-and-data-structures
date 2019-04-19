"""
Author: PyDev
Description: Singly Linked List without Tail consist of a element, where the element is the
			 skeleton and consist of a value and next variables.
			 There is a head pointer to refer to the front of the Linked List.
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
		"""
		self.value = value
		self.next = None

	def __repr__(self):
		return "element value = " + str(self.value)


class SinglyLinkedListWithoutTail:
	"""
	A class of Linked List where it have attributes and properties, such as:
		- Singly Linked List
		- Without tail
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
		- __repr__()
	"""
	def __init__(self, head = None):
		"""
		initilize SinglyLinkedListWithoutTail object instance

		Arguments:
			- head: default to None

		Instance variables:
			- head: an object value which refer to head/start of the Linked List
		"""
		self.head = head

	def pushFront(self, new_element):
		"""
		add new element to the front

		Arguments:
			- new_element: an object that reference to new element to be added
		"""
		if self.head:
			new_element.next = self.head
			self.head = new_element
		else:
			self.head = new_element

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
			self.head = self.head.next
		else:
			print("Singly Linked List Without Tail is empty!")

	def pushBack(self, new_element):
		"""
		add to back,also known as append

		Arguments:
			- new_element: an object that reference to new element to be added
		"""
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		else:
			self.head = new_element

	def topBack(self):
		"""
		return back/last element/item

		Returns:
			- the back/last element/item object
		"""
		current = self.head
		if self.head:
			while current.next:
				current = current.next
			return current
		else:
			print("Singly Linked List Without Tail is empty!")

	def popBack(self):
		"""
		remove back element/item
		"""
		previous = None
		current = self.head
		if self.head:
			while current.next:
				previous = current
				current = current.next
			previous.next = None
		else:
			print("Singly Linked List Without Tail is empty!")

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
			print("Singly Linked List Without Tail is empty!")

	def erase(self, value):
		"""
		remove an element/item from Linked List

		Arguments:
			- value: an object that represent a value we want to look for
		"""
		previous = None
		current = self.head
		while current.value != value and current.next:
			previous = current
			current = current.next
		if current.value == value:
			if previous:
				previous.next = current.next
			else:
				self.head = current.next

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

	def addBefore(self, new_element, position):
		"""
		add new element/item before a position in the Linked List

		Arguments:
			- new_element: an object that reference to a new element to be added
			- position: an object that reference to an integer object that tells the
						method to where place the new element/item
		"""
		count = 1
		current = self.head
		if position > 1:
			while current and count < position:
				if count == position - 1:
					new_element.next = current.next
					current.next = new_element
				current = current.next
				count += 1
		elif position == 1:
			new_element.next = self.head
			self.head = new_element

	def addAfter(self, new_element, position):
		"""
		add new element/item after a position in the Linked List

		Arguments:
			- new_element: an object that reference to a new element to be added
			- position: an object that reference to an integer object that tells the
						method to where place the new element/item
		"""
		count = 1
		current = self.head
		if position > 1:
			while current and count <= position:
				if count == position:
					new_element.next = current.next
					current.next = new_element
				current = current.next
				count += 1
		elif position == 1:
			new_element.next = self.head.next
			self.head.next = new_element

	def __repr__(self):
		current = self.head
		while current:
			print(current.__repr__())
			current = current.next