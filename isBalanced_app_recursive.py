"""
Author: PyDev
Description: Stack application where it check if a string is balanced with
             parentheses, brackets, and squiggly brackets using recursive
"""

from stack_using_array import Stack

def isBalanced(sentence_str, stack = None):
    sentence_str.replace(" ", "")
    if sentence_str:
        if sentence_str[0] in ['(', '[', '{']:
            stack.push(sentence_str[0])
            isBalanced(sentence_str[1:], stack)
        else:
            if stack.isEmpty():
                return False

            top = stack.pop()
            
            if (top == '[' and sentence_str[0] != ']') or \
               (top == '(' and sentence_str[0] != ')') or \
               (top == '{' and sentence_str[0] != '}'):
                return False
            isBalanced(sentence_str[1:], stack)
            
    return stack.isEmpty()
