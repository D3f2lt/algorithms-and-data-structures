"""
	Author: PyDev
	Description: Implementation of Binary Search Algorithm iteratively using Divide and Conquer
				 design paradigm to reduce the complexity and increase the efficiency
"""
def binary_search(list_obj, value, low, high):
	"""
		Iterative Binary Search Algorithm:
		Using Divide and Conquer design paradigm to reduce the complexity and increase the efficiency
		Arguments:
			list_obj: represent list object
			value: an object where it's value that we are looking for in the list
			low: an integer object it default to first index of the list
			high: an integer object it default to last index of the list
	"""
	while low <= high:
		middle = (low + high) // 2
		if value == list_obj[middle]:
			return True
		elif value > list_obj[middle]:
			low =  middle + 1
		else:
			high = middle - 1
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
		return binary_search(obj, value, 0, len(obj)-1)

list_obj = [3,5,7,9,11]
value = 11
print("Is", value, "in", list_obj, "?", search(list_obj,value))
