"""
-------------------------------------------------------
[Assignment 2, Task 5]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies,genre_counts
# Constants

fv = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fv)

counts = genre_counts(movies)

print(counts)