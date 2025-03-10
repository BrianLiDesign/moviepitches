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
        print("6. Current Preferences")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.set_user_mood()
            user.execute_recommendation()
        elif choice == "2":
            user.search_by_title()
        elif choice == "3":
            user.search_by_genre()
        elif choice == "4":
            user.search_by_rating()
        elif choice == "5":
            user.search_by_length()
        elif choice == "6":
            print(
                f"Current Preferences\n"
                f"Current Mood: {user.get_current_mood()}"
            )
        elif choice == "0":
            print("Exiting program.")
            user.running = False
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()