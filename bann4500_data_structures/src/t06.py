"""
-------------------------------------------------------
[Lab 3, Task 6]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-02-01"
-------------------------------------------------------
"""
# Imports
from utilities import list_test
from Movie_utilities import read_movies
# Constants

fh = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fh)

list_test(movies)