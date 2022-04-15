"""
-------------------------------------------------------
[Lab]
-------------------------------------------------------
Author:  John Bannan
ID:      200724500
Email:   bann4500@mylaurier.ca
__updated__ = "2021-01-18"
-------------------------------------------------------
"""
# Import
from Movie import *
# Constants

"""
-------------------------------------------------------
Movie class utility functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 B
__updated__ = "2021-01-12"
-------------------------------------------------------
"""


def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """

    title = str(input("Title: "))
    y_o_r = int(input("Year of release: "))
    director = str(input("Director: "))
    rat = float(input("Rating: "))
    
    print(""" Genres
 0 science fiction
 1 fantasy
 2 drama
 3 romance
 4 comedy
 5 zombie
 6 action
 7 historical
 8 horror
 9 war
10 mystery""")
    
    genre = int(input("Enter a genre number(Enter to quit): "))
    
    while genre != '':
        genre = int(input("Enter a genre number(Enter to quit): "))
    

    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    Data = line.strip().split('|')
    
    movie = Movie(Data[0], int(Data[1]), Data[2], float(Data[3]), [int(i) for i in Data[4].split(",")])

    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """

    """line = ' '
    movies = []

    while line != '':
        line = fv.readline().strip()
        movies.append(read_movie(line))"""

    movies=[]
    
    for line in fv:
        movie = read_movie(line.strip())
        movies.append(movie)
    
    return movies


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    print(Movie.genres_menu())
    
    dup = 0
    
    genres = []
    
    number = input("Enter a genre number (Enter to quit): ")
    
    while number != '' or genres == []:
        dup = 0
        if number.isdigit():
            number = int(number)
            if number>-1 and number<11:
                for value in genres:
                    if value == number:
                        print("Error")
                        dup += 1
                if dup==0:
                    genres.append(number)
                        
        else:
            print("Error")
        
        number = input("Enter a genre number (Enter to quit): ")
    
        
    genres.sort()
    
    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    The original list of movies must be unchanged.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is
            year (list of Movie)
    -------------------------------------------------------
    """
    
    ymovies = []
    
    for x in movies:
        if x.year == year:
            ymovies.append(x)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    The original list of movies must be unchanged.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """
    
    rmovies = []
    
    for x in movies:
        if x.rating >= rating:
            rmovies.append(x)
    
    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    The original list of movies must be unchanged.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    
    for x in movies:
        for y in x.genres:
            if y == genre:
                gmovies.append(x)

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    The original list of movies must be unchanged.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies= []
    
    genre_count = len(genres)
    
    for x in movies:
        if len(x.genres) == genre_count:
            num = 0
            for y in x.genres:
                for z in genres:
                    if  y == z:
                        num += 1
                        if num==2:
                            gmovies.append(x)

    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    The original list of movies must be unchanged.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    
    I0 = 0
    I1 = 0
    I2 = 0
    I3 = 0
    I4 = 0
    I5 = 0
    I6 = 0
    I7 = 0
    I8 = 0
    I9 = 0
    I10 = 0
    
    for x in movies:
        for y in x.genres:
            if y == 0:
                I0 += 1
            if y == 1:
                I1 += 1
            if y == 2:
                I2 += 1
            if y == 3:
                I3 += 1
            if y == 4:
                I4 += 1
            if y == 5:
                I5 += 1
            if y == 6:
                I6 += 1
            if y == 7:
                I7 += 1
            if y == 8:
                I8 += 1
            if y == 9:
                I9 += 1
            if y == 10:
                I10 += 1
                
    counts = [I0,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10]

    return counts

