# search_movies.py
# Author: Natalie Cartwright

import imdb
ia = imdb.IMDb()


#This searches the database of movies for a movie in the specified genre
#Genre is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_genre(genre: str) -> list[str]:
    #List of movie recommendations
    keyword = genre
    search = ia.get_keyword(keyword)
    return search
#def search_by_director(director: str) -> list[str]:
 #   movies = []
  #  keyword = director
   # search = ia.get_keyword(keyword)
    #movies.append(search)
    #return movies


#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str) -> list[str]:
    movies = ia.search_movie(title)
    return movies

#A function that searches for movies based on their ratings
#rating is an integer given by the user that they want to search for
#The function returns a list of movies that all have the specified rating given by the user
def search_by_rating(rating: int) -> list[str]:
    movies = []
    keyword = rating
    #Add if rating is above a threshold and search for all movies greater/equal to threshold


#A function that searches for movies depending on a specified length
#Length is an integer given by the user that they are searching for
#The function returns a list of movies all of that specified length
def search_by_length(length: int):
    #Same as above but use a time aspect instead of genre


#A function that searches for movies based on if they contain the specified person or not
#Person is an inputted string that the users wants to search for
#The function returns a list of movies containing the specified person
def search_by_person(person: str) -> list[str]:
    movies = []
    people = ia.search_person(person)
    for person in people:
    movies.append(person)


#Testing the functions


#Works
print(search_by_title("Avengers"))

#In progress
print(search_by_genre("dystopian"))