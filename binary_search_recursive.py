"""
	Author: PyDev
	Description: Implementation of Binary Search Algorithm recursivly using Divide and Conquer
				 design paradigm to reduce the complexity and increase the efficiency
"""


def binary_search(list_obj, value, low, high):
	"""
		Recursive Binary Search Algoirthm:
		Using Divide and Conquer design paradigm to reduce the complexity and increase the efficiency
		Arguments:
			list_obj: represent list object
			value: an object where it's value that we are looking for in the list
			low: an integer object it default to first index of the list
			high: an integer object it default to last index of the list
	"""
	if low == high:
		return list_obj[low] == value
	middle = (low + high) // 2
	if value == list_obj[middle]:
		return True
	elif value > list_obj[middle]:
		return binary_search(list_obj, value, middle + 1, high)
	else:
		return binary_search(list_obj, value, low, middle - 1)
	return False


def search(obj, value):
	"""
		Search if a value is inside an object
		Arguments:
			obj: represent an object to search inside it
			value: an object that we are looking for.
	"""
	if not obj:
		return False
	else:
		return binary_search(obj, value, 0, len(obj) - 1)


list_obj = [3,5,7,9,11]
value = 9
print("Is", value, "in", list_obj, "?", search(list_obj, value))
