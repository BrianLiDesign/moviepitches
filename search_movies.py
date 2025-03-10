# search_movies.py
# Author: Natalie Cartwright
import data



#This searches the database of movies for a movie in the specified genre
#keyword is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_genre(genre: str) -> list[str] | None:
    #List of movie recommendations
    movies = []
    for movie in data.movie_database:
        if movie not in data.movie_database:
            return None
        elif genre.lower() in movie['genre'].lower():
            movies.append(movie)
    return movies


#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str) -> list[str]| None:
    movies = []
    for movie in data.movie_database:
        if movie not in data.movie_database:
            return None
        elif title.lower() in movie['title'].lower():
            movies.append(movie)
    return movies

#A function that searches through movies based on their rating
#number is the rating that the user wants to search by
#This function returns a list of movies of the specified rating
def search_by_rating(rating: int) -> list[str] | None:
    movies = []
    for movie in data.movie_database:
        if movie not in data.movie_database:
            return None
        elif movie['rating'] >= rating:
            movies.append(movie)
    return movies

#A function that searches through movies based on their length
#length is an integer that the user wants to search by
#The function returns a list of movies of the specified length
def search_by_length(length: int) -> list[str] | None:
    movies = []
    for movie in data.movie_database:
        if movie not in data.movie_database:
            return None
        elif length <= movie['length'] <= 999:
            movies.append(movie)
    return movies






