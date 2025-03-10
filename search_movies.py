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

#A function that searches for movies based on their ratings
#rating is an integer given by the user that they want to search for
#The function returns a list of movies that all have the specified rating given by the user
def search_by_rating(min_rating: int) -> list[str]:
    top_movies = ia.get_top250_movies()
    for movie in top_movies[:3]:
        print(movie)

print(search_by_rating(5))


#A function that searches for movies depending on a specified length
#Length is an integer given by the user that they are searching for
#The function returns a list of movies all of that specified length
def search_by_length(length: int):
    movies = ia.get_top250_movies()
    return [movie['title'] for movie in movies if movie.get('runtimes') and int(movie['runtimes'][0]) == length]







