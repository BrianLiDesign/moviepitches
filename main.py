# main.py
# Author: Brian Li
from setup import UserInput
from search_movies import search_by_keyword


# Runs the main menu loop, allowing the user to set preferences, get movie recommendations, or exit.
def main():
    user = UserInput()
    while user.running:
        print("\nMovie Pitcher")
        print("1. Get Recommended Movies")
        print("2. Modify Preferences")
        print("3. Current Preferences")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user.execute_recommendation()
        if choice == "2":
            user.set_user_preferences()
        if choice == "3":
            print(repr(user))
        if choice == "5":
            print("Exiting program.")
            user.running = False


if __name__ == "__main__":
    main()