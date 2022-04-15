"""
-------------------------------------------------------
[Assignment 9, Task 3]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-04-02"
-------------------------------------------------------
"""
# Imports
from functions import insert_words, comparison_total
from Hash_Set_BST import Hash_Set
from Word import Word


hash_set = Hash_Set(20)
fv = open("miserables.txt", 'r')
insert_words(fv, hash_set)
total, max_word = comparison_total(hash_set)


print("Using linked BST Hash_Set")

print("Total Comparisons: {}".format(total))
print("Word with maximum comparisons {}".format(max_word))