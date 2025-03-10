# main.py
# Author: Brian Li
from setup import UserInput
import search_movies


# Runs the main menu loop, allowing the user to set preferences, get movie recommendations, or exit.
def main():
    user = UserInput()
    while user.running:
        print("\nMovie Pitcher")
        print("1. Search Based on Your Mood")
        print("2. Search by Title")
        print("3. Search by Genre")
        print("4. Search by Rating")
        print("5. Search by Length")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.execute_recommendation()
        if choice == "2":
            user.set_user_preferences()
        if choice == "3":
            print(repr(user))
        if choice == "4":
            genre = input("Enter Genre: ")
            movies_by_genre = search_movies.search_by_genre(genre)
            print("\nMovies in Genre:")
            for movie in movies_by_genre:
                print(f"- {movie["title"]}")
        if choice == "10":
            print("Exiting program.")
            user.running = False


if __name__ == "__main__":
    main()