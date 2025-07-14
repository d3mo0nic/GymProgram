import json

class Gymlogin:
    '''
    This class handles the login for the gym module.
    It checks if the user is an admin and allows them to create a new email and password,
    if they are not already set. It also checks the strength of the password
    if the password is not strong enough, it prompts the user to create a new one.

    Attributes:
        email : The email of user.
        password : The password of user.
    Methods:
        check_login(): Prompts the user for email and password, checks against stored credentials.
        is_strong(password): Checks if the password meets strength requirements.
    '''
    def __init__(self):
        with open("gymapp/data/passwords.json", "r") as f:
            passwords = json.load(f)
        if passwords[0]["password"] == "Admin" and passwords[0]["user_id"] == "Admin":
            self.email = input("Please create new email: ")
            self.password = input("Please create new password: ")
            strong = Gymlogin.is_strong(self.password)
            while strong == False:
                print('❌Password not strong enough (include one digit, one uppercase, one special character and 8 or more characters)❌')
                self.email = input("Please create new email: ")
                self.password = input("Please create new password: ")
                strong = Gymlogin.is_strong(self.password)
            with open("gymapp/data/passwords.json", "w") as f:
                json.dump([{'password': self.password, 'email': self.email}], f, indent=4)
        
    def check_login(self):
        print('🔏 Please Login to Gym Module')
        for i in range(3):
            give_email = input("Enter your Email: ")
            give_password = input("Enter your Password: ")
            with open("gymapp/data/passwords.json", "r") as f:
                password = json.load(f)
            if password[0]["email"] == give_email and password[0]["password"] == give_password:
                print('✅ Login succesfull')
                return True
            else:
                print('❌ Email or password incorrect!')
                print(f'You have {2 - i} chances left')
        print('Too many failed Attempts!')
        return False
    @staticmethod
    def is_strong(password):
        return (
            len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%^&*()-_=+[]{}|;:'/',.<>?/`~" for char in password)
        )