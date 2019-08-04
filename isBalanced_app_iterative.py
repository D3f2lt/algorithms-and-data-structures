"""
Author: PyDev
Description: Stack application where it check if a string is balanced with
             parentheses, brackets, and squiggly brackets using iterative
"""

from stack_using_linked_list import Stack

def isBalanced(sentence_str):
    stack = Stack()
    sentence_str = sentence_str.replace(" ", "")
    for char in sentence_str:
        if char in ['(', '[', '{']:
            stack.push(char)
        else:
            if stack.isEmpty(): return False
            top = stack.pop()
            if (top == '[' and char != ']') or \
               (top == '(' and char != ')') or \
               (top == '{' and char != '}'): \
                return False
    return stack.isEmpty()
