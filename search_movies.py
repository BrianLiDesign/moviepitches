# search_movies.py
# Author: Natalie Cartwright

import imdb
ia = imdb.IMDb()


#This searches the database of movies for a movie in the specified genre
#keyword is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_keyword(keyword: str) -> list[str]:
    #List of movie recommendations
    movies = ia.search_keyword(keyword)
    return [movies['title'] for movie in movies]



#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str) -> list[str]:
    movies = ia.search_movie(title)
    return movies

#A function that searches for movies based on their ratings
#rating is an integer given by the user that they want to search for
#The function returns a list of movies that all have the specified rating given by the user
def search_by_rating(min_rating: int) -> list[str]:
    top_movies = ia.get_top250_movies()
    return [movie['title'] for movie in top_movies if movie.get('rating',0) >= min_rating]


#A function that searches for movies depending on a specified length
#Length is an integer given by the user that they are searching for
#The function returns a list of movies all of that specified length
def search_by_length(length: int):
    movies = ia.get_top250_movies()
    return [movie['title'] for movie in movies if movie.get('runtimes') and int(movie['runtimes'][0]) == length]


# This search the database for movies with a specified director
# director is string that is inputted by the user that they want to search for
# This function returns a list of movies containing the inputted director
def search_by_director(director: str) -> list[str]:
    search = ia.search_person(director)
    if not search:
        return []
    director_id = search[0].personID
    director_info = ia.get_person_filmography(director_id)

    if 'director' in director_info['data']['filmography']:
        return [movie['title'] for movie in director_info['data']['filmography']['director']]
    else:
        return []


# A function that searches for movies based on if they contain the specified person or not
# Person is an inputted string that the users wants to search for
# The function returns a list of movies containing the specified person
def search_by_person(person: str) -> list[str]:
    people = ia.search_person(person)
    if not people:
        return []

    person_id = people[0].personID
    person_info = ia.get_person(person_id)

    if 'filmography' in person_info.data:
        filmography = person_info['filmography']
        movies = []
        for category in filmography:
            for movie in filmography[category]:
                movies.append(movie['title'])
            return movies
    else:
        return []


