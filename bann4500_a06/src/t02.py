"""
-------------------------------------------------------
[Assignment 6, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-03-11"
-------------------------------------------------------
"""
#imports
from List_linked import List
from Movie_utilities import read_movies
from utilities import list_test
# Constants

fh = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fh)

list_test(movies)