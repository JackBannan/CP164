"""
-------------------------------------------------------
[Assignment 8, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-25"
-------------------------------------------------------
"""
# Imports

# Constants

from BST_linked import BST
from Letter import Letter
from functions import do_comparisons, comparison_total, letter_table

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

tree1 = BST()
tree2 = BST()
tree3 = BST()

for char in DATA1:
    l = Letter(char)
    tree1.insert(l)

for char in DATA2:
    l = Letter(char)
    tree2.insert(l)

for char in DATA3:
    l = Letter(char)
    tree3.insert(l)




txtfile = open("miserables.txt", "r")
do_comparisons(txtfile, tree1)
txtfile = open("miserables.txt", "r")
do_comparisons(txtfile, tree2)
txtfile = open("miserables.txt", "r")
do_comparisons(txtfile, tree3)

txtfile.close()

total1 = comparison_total(tree1)
total2 = comparison_total(tree2)
total3 = comparison_total(tree3)

letter_table(tree1)
letter_table(tree2)
letter_table(tree3)

print("""
Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Total Comparisons: {:,}
------------------------------------------------------------
Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ
Total Comparisons: {:,}
------------------------------------------------------------
Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ
Total Comparisons: {:,}
""".format(total1, total2, total3))