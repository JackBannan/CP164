"""
-------------------------------------------------------
[Assignment 2, Task 2]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_rating,read_movies
# Constants

fv = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fv)

rating = 8.00

rmovies = get_by_rating(movies, rating)

for x in rmovies:
    print(x)
    print()