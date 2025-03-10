# setup.py
# Author: Brian Li
import search_movies
import data
from sentiment_analysis import sentiment_analysis, set_genre


# Handles mood validation for user input of mood
def validate_mood(mood):
    return mood.isalpha() or mood == ""

# Handles number validation for user input of movie duration
def validate_number(num, min_value, max_value):
    return num.isdigit() and min_value <= int(num) <= max_value

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

    def __repr__(self):
        """Returns a formatted string representation of the user's preferences."""
        return (
            f"\nCurrent Preferences:\n"
            f"  Mood: {self.user_mood}"
        )

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
            movies.append(movie)
        if not movies:
            print("\nNo movies found that match your criteria.")
            return

        print("\nRecommended Movies:")
        for movie in movies:
            print(f"- {movie}")