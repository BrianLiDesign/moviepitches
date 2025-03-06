# setup.py
# Author: Brian Li
# import search_movies

# A class that handles user input for movie recommendations based on preferences.
class UserInput:
    # Initializes the UserInput object with default preferences.
    def __init__(self):
        self.running = True
        self.user_mood = None
        self.user_min_length = 0
        self.user_max_length = 1000
        self.user_min_rating = 0

    # Returns a string representation of the user's current preferences.
    def __str__(self):
        return (f"The user's mood is {self.user_mood}"
                f"The user's minimum length is {self.user_min_length}"
                f"The user's maximum length is {self.user_max_length}"
                f"The user's minimum rating is {self.user_min_rating}")

    # Returns a formal string representation of the user's preferences.
    def __repr__(self):
        return (f"User Preferences: {self.user_mood}, "
                f"Min Length: {self.user_min_length}, "
                f"Max Length: {self.user_max_length}, "
                f"Min Rating: {self.user_min_rating}")

    # def validation
    # Maybe function ?
    # Maybe just use try and exception handlers in set_user_preferences

    # Prompts the user to enter their movie preferences, including mood, minimum and maximum length, and minimum rating.
    def set_user_preferences(self):
        self.user_mood = input("Describe your mood or press Enter to skip: ")
        self.user_min_length = int(input("Enter minimum movie length (or 0 to skip): "))
        self.user_max_length = int(input("Enter maximum movie length (or 999 to skip): "))
        self.user_min_rating = float(input("Enter minimum rating (or 0 to skip): "))


    # Generates and displays a list of recommended movies based on the user's preferences.
    # Inputs: relies on previously set user preferences
    # Output: calls a movie recommendation function, prints the recommended movies, and prompts the user to restart or exit.
    def execute_recommendation(choice: int):
        movies = []
        # search_movies.py code goes here
        #
        print("Recommended Movies:")
        for movie in movies:
            print(movie)
        choice = input("Enter 1 to restart and enter 0 to quit: ")
        if choice == "1":
            UserInput().run()
        elif choice == "0":
            self.running = False
        else:
            print("Invalid input. Please try again.")

    # Runs the main menu loop, allowing the user to set preferences, get movie recommendations, or exit.
    def run(self):
        print("\nMovie Pitcher")
        print("1. Set User Preferences")
        print("2. Get a list of movies")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            self.set_user_preferences()
        if choice == "2":
            self.execute_recommendation()
        elif choice == "3":
            print("Exiting program.")
            self.running = False
        else:
            print("Invalid choice. Please try again.")