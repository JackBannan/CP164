"""
-------------------------------------------------------
[Assignment 2, Task 4]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies,get_by_genres
# Constants

fv = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fv)

genres = [0,6]

m = get_by_genres(movies, genres)

for x in m:
    print(x)