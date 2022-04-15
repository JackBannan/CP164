"""
-------------------------------------------------------
[Assignment 2, Task 3]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-28"
-------------------------------------------------------
"""
# Imports
from Movie_utilities import read_movies,get_by_genre
# Constants


fv = open('movies.txt', 'r', encoding="utf-8")

movies = read_movies(fv)

genre = 9

gmovies = get_by_genre(movies, genre)

for x in gmovies:
    print(x)