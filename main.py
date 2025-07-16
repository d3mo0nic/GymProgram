from login import Gymlogin
import json
from gym import Gym, add_new_member

# Main program execution
# Initialize the Gymlogin class to handle user login
login = Gymlogin()

# Check if the user can log in
# If login is successful, load gym members and display the main menu
if login.check_login():
    # Upload previously saved members from the json file
    Gym.load_file()
    while True:
        print("\n🔧 Main Menu:")
        print("1. View All Members")
        print("2. View Unpaid Members")
        print("3. View Paid Members")
        print("4. Add a New Member")
        print("5. Revoke Membership")
        print("6. Block Unpaid Member")
        print("0. Exit\n")
        # Prompt the user for their choice
        print("Please choose an option (1-6 or 0 to exit):")
        choice = input("")
        if choice == "1":
            Gym.show_members()
        elif choice == "2":
            Gym.show_members("unpaid")
        elif choice == "3":
            Gym.show_members("paid")
        elif choice == "4":
            add_new_member()
        elif choice == "5":
            Gym.revoke_member()
        elif choice == "6":
            Gym.block_members()
        elif choice == "0":
            print("Thank you , Goodbye !")
            break
        else :
            print("Invalid input ! please choose from 1 - 6 ")
else:
    print('Exiting Program')