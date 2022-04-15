"""
-------------------------------------------------------
[Assignment 2, Task 1]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import get_by_year,read_movies
# Constants

fv = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fv)

year = 2013

ymovies = get_by_year(movies, year)

for x in ymovies:
    print(x)