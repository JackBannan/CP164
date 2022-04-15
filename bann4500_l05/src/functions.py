"""
-------------------------------------------------------
[Lab 5]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-18"
-------------------------------------------------------
"""
# Imports

# Constants

def recurse(x, y):
    """
    -------------------------------------------------------
    Recursive function - example of tree recursion.
    Use: ans = recurse(x, y)
    -------------------------------------------------------
    Parameters:
        x - an integer (int)
        y - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if x < 0 or y < 0: 
        ans = x - y
    else:
        ans = recurse(x-1,y) + recurse(x,y-1)
    
    return ans

def gcd(m, n):
    """
    -------------------------------------------------------
    Recursively find the Greatest Common Denominator of two numbers.
    Use: ans = gcd(m, n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int)
        m - an integer (int)
    Returns:
        ans - the function result (int)
    -------------------------------------------------------
    """
    
    if m%n == 0:
        ans = n
    else:
        ans = gcd(n, m % n)
    
    return ans


def vowel_count(s):
    """
    -------------------------------------------------------
    Recursively counts number of vowels in a string.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - string to examine (str)
    Returns:
        count - number of vowels in s (int)
    -------------------------------------------------------
    """
    
    vowels = "aeiouAEIOU"
    count = 0
    
    n = len(s)
    
    if n>0:
        if s[0].lower() in vowels:
            count = count+1
        s = s[1:]
        count = count+vowel_count(s)
    
    
    return count


def to_power(base, power):
    """
    -------------------------------------------------------
    Calculates base^power.
    Use: ans = to_power(base, power)
    -------------------------------------------------------
    Parameters:
        base - base to apply power to (float)
        power - power to apply (int)
    Returns:
        ans - base ^ power (float)
    -------------------------------------------------------
    """

    if power == 0:
        ans = 1
    elif power<0:
        ans = 1/to_power(base, -power)
    else:
        ans = base*to_power(base, power-1)
    
    return ans


def is_palindrome(s):
    """
    -------------------------------------------------------
    Recursively determines if s is a palindrome. Ignores non-letters and case.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    n = len(s)
    
    if n==1:
        palindrome = True
    elif n>1:
        if s[0].isalpha() == False:
            s = s[1:]
            palindrome = is_palindrome(s)
        elif s[-1].isalpha() == False:
            s = s[:-1]
            palindrome = is_palindrome(s)

        elif s[0].lower() != s[-1].lower():
            palindrome = False
        else:
            s = s[1:-1]
            
            palindrome = is_palindrome(s)
    else:
        palindrome = True
            
    
    return palindrome

def bag_to_set(bag):
    """
    -------------------------------------------------------
    Copies elements of a bag to a set.
    Use: new_set = bag_to_set(bag)
    -------------------------------------------------------
    Parameters:
        bag - a list of values (list)
    Returns:
        new_set - containing one each of the elements in bag (list)
    -------------------------------------------------------
    """
    
    n = len(bag)
    
    
    '''if n>0:
        if bag[0] not in new_set:
            new_set.append(bag[0])
        bag = bag[1:]
        new_set = new_set+bag_to_set(bag)'''
    
    if n==0:
        new_set = []
    elif bag[-1] in bag[:-1]:
        new_set = bag_to_set(bag[:-1])
    else:
        new_set =  bag_to_set(bag[:-1])+[bag[-1]]
    
    return new_set
