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
        self.user_min_length = 0
        self.user_max_length = 999
        self.user_min_rating = 0.0

    # Returns a string representation of the user's current preferences.
    def __str__(self):
        return (f"User Preferences:\n"
            f"- Mood: {self.user_mood}, "
            f"- Min Length: {self.user_min_length}\n"
            f"- Max Length: {self.user_max_length}\n"
            f"- Min Rating: {self.user_min_rating}")

    def __repr__(self):
        """Returns a formatted string representation of the user's preferences."""
        return (
            f"\nCurrent Preferences:\n"
            f"  Mood: {self.user_mood}\n"
            f"  Min Length: {self.user_min_length} mins\n"
            f"  Max Length: {self.user_max_length} mins\n"
            f"  Min Rating: {self.user_min_rating}"
        )

    # Prompts the user to enter their movie preferences, including mood, minimum and maximum length, and minimum rating.
    def set_user_preferences(self):
        while True:
            mood = input("Describe your mood or press Enter to skip: ")
            if validate_mood(mood):
                self.user_mood = mood
                break
            print("Invalid mood. Please enter only letters.")

        while True:
            min_length = input("Enter minimum movie length between 0 - 999 (or 0 to skip): ")
            if validate_number(min_length, 0, 999):
                self.user_min_length = int(min_length)
                break
            print("Invalid length. Please enter a number between 0 and 999.")

        while True:
            max_length = input("Enter maximum movie length (or 999 to skip): ")
            if validate_number(max_length, self.user_min_length, 999):
                self.user_max_length = int(max_length)
                break
            print("Invalid length. Please enter a number greater than the minimum length and up to 999.")

        while True:
            min_rating = input("Enter minimum rating (or 0 to skip): ")
            if validate_number(min_rating, 0, 10):
                self.user_min_rating = int(min_rating)
                break
            print("Invalid rating. Please enter a number between 0 and 10.")

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
        movies = search_movies.search_by_preferences(genres, self.user_min_rating, self.user_min_length, self.user_max_length)

        if not movies:
            print("\nNo movies found that match your criteria. Try adjusting your preferences.")
            return

        print("\nRecommended Movies:")
        for movie in movies:
            print(f"- {movie}")