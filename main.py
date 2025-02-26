# main.py
# Author: Brian Li
class MoviePitcher:
    def __init__(self):
        self.running = True
        self.user_mood = None
        self.user_min_length = 0
        self.user_max_length = 1000
        self.user_min_rating = 0

    # def validation
    # Maybe function ?
    # Maybe just use try and exception handlers in set_user_preferences

    def set_user_preferences(self):
        self.user_mood = input("Describe your mood or press Enter to skip: ")
        self.user_min_length = int(input("Enter minimum movie length (or 0 to skip): "))
        self.user_max_length = int(input("Enter maximum movie length (or 999 to skip): "))
        self.user_min_rating = float(input("Enter minimum rating (or 0 to skip): "))

    def execute_recommendation(self):
        movies = []
        # movie_suggestions.py code goes here
        print("Recommended Movies:")
        for movie in movies:
            print(movie)
        choice = input("Enter 1 to restart and enter 0 to quit: ")
        if choice == "1":
            MoviePitcher().run()
        elif choice == "0":
            self.running = False
        else:
            print("Invalid input. Please try again.")

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


if __name__ == '__main__':
    MoviePitcher().run()