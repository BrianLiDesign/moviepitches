# search_movies.py
# Author: Natalie Cartwright

import imdb
ia = imdb.IMDb()


#This searches the database of movies for a movie in the specified genre
#keyword is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_keyword(keyword: str) -> list[str]:
    #List of movie recommendations
    movies = ia.search_movie(keyword)

    movie_titles = [str(movie) for movie in movies]
    return movie_titles


#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str) -> list[str]:
    movies = ia.search_movie(title)
    movie_titles = [str(movie) for movie in movies]
    return movie_titles


def search_by_rating(number: int) -> list[str]:





