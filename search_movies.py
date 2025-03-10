# search_movies.py
# Author: Natalie Cartwright




#This searches the database of movies for a movie in the specified genre
#keyword is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_keyword(genre: str, movie_database) -> list[str]:
    #List of movie recommendations
    movies = []
    for movie in movie_database:
        if movie.genre.lower() == genre.lower():
            movies.append(movie)
    return movies




#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if movie.title.lower() == title.lower():
            movies.append(movie)
    return movies


def search_by_rating(number: int, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if movie.rating >= number:
            movies.append(movie)
    return movies

def search_by_length(length: int, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if movie.length >= length:
            movies.append(movie)
    return movies





