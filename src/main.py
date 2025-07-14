from login import Gymlogin
import json
from gym import Gym, add_new_member

login = Gymlogin()

if login.check_login():
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