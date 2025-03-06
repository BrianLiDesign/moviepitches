import imdb
ia = imdb.IMDb()

def search_by_genre(genre: str) -> list[str]:
    #List of movie recommendations
    movies = []

    #Accessing the movies by keyword being the genre
    keyword = genre
    search = ia.get_keyword(keyword)
    movies.append(search)
    return movies

def search_by_director(director: str) -> list[str]:
    movies = []
    keyword = director
    search = ia.get_keyword(keyword)
    movies.append(search)
    return movies

def search_by_title(title: str) -> list[str]:
    movies = []
    keyword = title
    search = ia.get_keyword(keyword)
    movies.append(search)
    return movies

def search_by_rating(rating: int) -> list[str]:
    movies = []
    keyword = rating
    #Add if rating is above a threshold and search for all movies greater/equal to threshold

def search_by_length(length: int):
    #Same as above but use a time aspect instead of genre





