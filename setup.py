# setup.py
# Author: Brian Li
import data
import search_movies
from sentiment_analysis import sentiment_analysis, set_genre


# The function handles mood validation for user input of mood
# Input: A string representing the user's mood.
# Output: Returns True if the mood contains only alphabetic characters or is an empty string, otherwise False.
def validate_mood(mood):
    return mood.isalpha() or mood == ""

# A class that handles user input for movie recommendations based on preferences.
class UserInput:
    # Initializes the UserInput object with default preferences.
    def __init__(self):
        self.running = True
        self.user_mood = None

    # Returns a string representation of the user's current preferences.
    def __str__(self):
        return (f"User Preferences:\n"
            f"- Mood: {self.user_mood}"
        )

    # Returns a formatted string representation of the user's preferences.
    def __repr__(self):
        return (
            f"\nCurrent Preferences:\n"
            f"  Mood: {self.user_mood}"
        )

    # Sets the user's mood preference.
    def set_user_mood(self):
        mood = input("Enter your mood: ").strip()
        if validate_mood(mood):
            self.user_mood = mood
        else:
            print("Invalid mood input. Please use only alphabetic characters.")

    # Generates and displays a list of recommended movies based on the user's preferences.
    # Inputs: relies on previously set user preferences
    # Output: calls a movie recommendation function, prints the recommended movies, and prompts the user to restart or exit.
    def execute_recommendation(self):
        if self.user_mood:
            mood_category = sentiment_analysis(self.user_mood)
            genres = set_genre(mood_category)
        else:
            genres = (data.genres_very_positive + data.genres_positive + data.genres_neutral + data.genres_negative +
                      data.genres_very_negative)

        movies = []
        for genre in genres:
            movie = search_movies.search_by_genre(genre)
            if movie:
                movies.extend(movie)

        if not movies:
            print("\nNo movies found that match your criteria.")
            return

        print("\nRecommended Movies:")
        for movie in movies:
            print(f"- {movie["title"]} (Genre: {movie["genre"]}, Rating: {movie["rating"]}, Length: {movie["length"]} mins)")

    # Searches movies by title and displays the results.
    def search_by_title(self):
        title = input("Enter the movie title: ").strip()
        movies_by_title = search_movies.search_by_title(title)
        if movies_by_title:
            print("\nMovies Found:")
            for movie in movies_by_title:
                print(f"- {movie["title"]} (Genre: {movie["genre"]}, Rating: {movie["rating"]}, Length: {movie["length"]} mins)")
        else:
            print("\nNo movies found with that title.")

    # Searches movies by genre and displays the results.
    def search_by_genre(self):
        genre = input("Enter the genre: ").strip()
        movies_by_genre = search_movies.search_by_genre(genre)
        if movies_by_genre:
            print("\nMovies in Genre:")
            for movie in movies_by_genre:
                print(f"- {movie["title"]} (Genre: {movie["genre"]}, Rating: {movie["rating"]}, Length: {movie["length"]} mins)")
        else:
            print("\nNo movies found in that genre.")

    # Searches movies by rating and displays the results.
    def search_by_rating(self):
        while True:
            self.user_min_rating = input("Enter a minimum rating between 0 - 10: ").strip()
            if not self.user_min_rating.isdigit():
                print("Please enter a number for rating.")
                continue
            elif int(self.user_min_rating) < 0 or int(self.user_min_rating) > 10:
                print("Please enter a number between 0 - 10")
                continue
            break
        movies_by_rating = search_movies.search_by_rating(int(self.user_min_rating))
        if movies_by_rating:
            print("\nMovies with Rating:")
            for movie in movies_by_rating:
                print(f"- {movie["title"]} (Genre: {movie["genre"]}, Rating: {movie["rating"]}, Length: {movie["length"]} mins)")
        else:
            print("\nNo movies found with that rating.")

    # Searches movies by length and displays the results.
    def search_by_length(self):
        while True:
            self.user_min_length = input("Enter minimum movie length between in minutes 1 - 999: ")
            if not self.user_min_length.isdigit():
                print("Please enter a number for movie length.")
                continue
            if not int(self.user_min_length) > 0 or not int(self.user_min_length) <= 999:
                print("Please enter a valid length between 1 and 999.")
                continue
            break
        movies_by_length = search_movies.search_by_length(int(self.user_min_length))
        if movies_by_length:
            print("\nMovies with Length:")
            for movie in movies_by_length:
                print(f"- {movie["title"]} (Genre: {movie["genre"]}, Rating: {movie["rating"]}, Length: {movie["length"]} mins)")
        else:
            print("\nNo movies found within that length.")