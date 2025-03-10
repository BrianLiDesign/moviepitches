# search_movies.py
# Author: Natalie Cartwright




#This searches the database of movies for a movie in the specified genre
#keyword is a string that is inputted by the user that they want to search for
#the function returns a list of movies that are in the given genre
def search_by_genre(genre: str, movie_database) -> list[str]:
    #List of movie recommendations
    movies = []
    for movie in movie_database:
        if genre.lower() in movie['genres'].lower():
            movies.append(movie)
    return movies


#A function that search through the IMDB database for movies with the given title
#title is a string and is the title of the movie that the user is searching for
#The function returns both the movie ID and movie title
def search_by_title(title: str, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if title.lower() in movie['title'].lower():
            movies.append(movie)
    return movies

#A function that searches through movies based on their rating
#number is the rating that the user wants to search by
#This function returns a list of movies of the specified rating
def search_by_rating(rating: int, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if movie['rating'] >= rating:
            movies.append(movie)
    return movies

#A function that searches through movies based on their length
#length is an integer that the user wants to search by
#The function returns a list of movies of the specified length
def search_by_length(length: int, movie_database) -> list[str]:
    movies = []
    for movie in movie_database:
        if length <= movie['length'] <= 999:
            movies.append(movie)
    return movies

#A function that gets user input for how they want to search and then does that search
#user_input is an integer that indicates the users choice
#This function returns a list of movies based on the search the user did
def search(user_input: int) -> list[str]:
    user_input = input("How would you like to search: 1: By genre, 2: By tile, 3: By rating, 4: By length: ")
    if user_input == "1":
        genre = input("Enter genre: ")
        search_by_genre(genre, movie_database)
    elif user_input == "2":
        title = input("Enter title: ")
        search_by_title(title, movie_database)
    elif user_input == "3":
        rating = int(input("Enter rating: "))
        search_by_rating(rating, movie_database)
    elif user_input == "4":
        length = int(input("Enter length: "))
        search_by_length(length, movie_database)
    else:
        return []



