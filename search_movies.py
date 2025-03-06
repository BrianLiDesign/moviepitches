import imdb
ia = imdb.IMDb()

def search_by_genre(genre: str) -> list[str]:
    #List of movie recommendations

    movies = ia.get_keyword(genre)
    return movies

#def search_by_director(director: str) -> list[str]:
 #   movies = []
  #  keyword = director
   # search = ia.get_keyword(keyword)
    #movies.append(search)
    #return movies


#A function that search through the IMDB database for movies with the given title
#and returns both the movie ID and movie title
def search_by_title(title: str) -> list[str]:
    movies = ia.search_movie(title)
    return movies

#def search_by_rating(rating: int) -> list[str]:
 #   movies = []
  #  keyword = rating
    #Add if rating is above a threshold and search for all movies greater/equal to threshold

#def search_by_length(length: int):
    #Same as above but use a time aspect instead of genre

#def search_by_person(person: str) -> list[str]:
 #   movies = []
  #  people = ia.search_person(person)
   # for person in people:
    #    movies.append(person)

#Works
#print(search_by_title("Avengers"))

print(search_by_genre("dystopian"))