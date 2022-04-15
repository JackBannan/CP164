"""
-------------------------------------------------------
[Assignment 3]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-01"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from utilities import array_to_stack
# Constants

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    
    while not source.is_empty():
        target1.push(source.pop())
        if source.is_empty() == False:
            target2.push(source.pop())
    
    return target1, target2

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    stack_list = []
    
    while not source.is_empty():
        value = source.pop()
        stack_list.insert(0,value)
    
    array_to_stack(source, stack_list)
    
    return 


# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    s = Stack()
    
    for x in string:
        
        if x == "+":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)+float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "-":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)-float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "*":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)*float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == "/":
            v1 = s.pop()
            v2 = s.pop()
            new_v = float(v1)/float(v2)
            print(new_v)
            s.push(new_v)
            
        elif x == " ":
            pass
            
        else:
            s.push(x)
    
    answer = s.pop()
    
    return answer


def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    
    
    
    
    
    
    
    
    
    return







# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    assert m not in valid_chars, \
        "cannot use '{}' as the mirror character".format(m)
        
    mirror = True
    stack = Stack()
    n = len(string)
    i = 0
    
    while mirror and i < n and string[i] != m:
        
        if not string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = False
            
    if mirror:
        
        i += 1
        
        while mirror and i > n and not stack.is_empty():
            c = stack.pop()
            
            if string[i] != c:
                mirror = False
            else:
                i += 1
                
        if not (stack.is_empty() and i == n):
            mirror = False
        
    return mirror








