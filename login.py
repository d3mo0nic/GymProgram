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
        ''' Initializes the Gymlogin class.
        
        Args:
            self: The class instance.
        
        If the passwords.json file does not exist or is empty, it prompts the user to create a new email and password.
        If the password is not strong enough, it prompts the user to create a new one.'''
        # Checks if the passwords.json file exists
        with open("gymapp/data/passwords.json", "r") as f:
            passwords = json.load(f)
        # If file contains no passwords, just admin credentials, prompts user to create a new email and password
        if passwords[0]["password"] == "Admin" and passwords[0]["user_id"] == "Admin":
            self.email = input("Please create new email: ")
            self.password = input("Please create new password: ")
            # Checks if the password is strong enough
            strong = Gymlogin.is_strong(self.password)
            # If not strong enough, prompts user to create a new one
            while strong == False:
                print('❌Password not strong enough (include one digit, one uppercase, one special character and 8 or more characters)❌')
                self.email = input("Please create new email: ")
                self.password = input("Please create new password: ")
                strong = Gymlogin.is_strong(self.password)
            # Saves the new email and password to the passwords.json file
            with open("gymapp/data/passwords.json", "w") as f:
                json.dump([{'password': self.password, 'email': self.email}], f, indent=4)
        
    def check_login(self):
        ''' Checks if the user can log in to the gym module.
        Args:
            self: The class instance.
        Returns:
            bool: True if login is successful, False otherwise.'''
        print('🔏 Please Login to Gym Module')
        # Prompts the user for email and password
        for i in range(3):
            give_email = input("Enter your Email: ")
            give_password = input("Enter your Password: ")
            with open("gymapp/data/passwords.json", "r") as f:
                password = json.load(f)
            # Alows for 3 attempts to enter correct email and password
            # If the email and password match the stored credentials, login is successful
            if password[0]["email"] == give_email and password[0]["password"] == give_password:
                print('✅ Login succesfull')
                return True
            else:
                print('❌ Email or password incorrect!')
                print(f'You have {2 - i} chances left')
        # If the user fails to log in after 3 attempts, the program exits
        print('Too many failed Attempts!')
        return False
    @staticmethod
    def is_strong(password):
        ''' Checks if the password is strong enough.
        Returns:
            bool: True if the password is strong, False otherwise.
        '''
        return (
            # Checks if the password is at least 8 characters long,
            len(password) >= 8 and
            # Contains at least one uppercase letter,
            any(char.isupper() for char in password) and
            # Contains at least one digit,
            any(char.isdigit() for char in password) and
            # Contains at least one special character,
            any(char in "!@#$%^&*()-_=+[]{}|;:'/',.<>?/`~" for char in password)
        )