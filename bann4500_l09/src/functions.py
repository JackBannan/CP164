"""
-------------------------------------------------------
[Lab 9]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-20"
-------------------------------------------------------
"""
# Imports

# Constants
def __hash__(self):
        """
        -------------------------------------------------------
        Generates a hash value from a movie name.
        Use: h = hash(movie)
        -------------------------------------------------------
        Returns:
            returns
            value - the total of the characters in the name string
                multiplied by the year (int > 0)
        -------------------------------------------------------
        """
        value = 0

        for c in self.title:
            value = value + ord(c)
        value *= self.year
        return value


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    
    print("Hash     Slot Key")
    for x in values: 
        value = 0

        for c in x.title:
            value = value + ord(c)
        value *= x.year    
        slot = value%7
        print("{}    {} {}, {}".format(value,slot,x.title,x.year))
    
    return





