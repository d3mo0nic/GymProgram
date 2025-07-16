import json

class Gym:
    '''
    This class handles the gym members and their membership status. It allows adding new members, viewing all members, viewing unpaid and paid members,
    revoking membership, and blocking unpaid members.

    Attributes:
        member: A list of GymMember instances.
    Methods:    
        show_members(filter=None): Displays all members or filters by paid/unpaid status.
        revoke_member(): Revokes membership of a member based on their birthdate.
        block_members(): Blocks all unpaid members.
        add_member(name, birthdate, is_paid): Adds a new member to the gym.
        convert_dict(): Converts the member to a dictionary.
        load_file(): Loads members from a json file.
        save_to_file(): Saves members to a json file.    
    
    Arguments:
        name : The name of the member.
        birthdate : The birthdate of the member.
        is_paid : The payment status of the member.
        is_active : The active status of the member.
        is_blocked : The blocked status of the member.
    '''
    members = []
    def __init__(self, name, birthdate, is_paid, is_active = True, is_blocked = False):
        ''' 
        Initializes a Gym member with their details.
        Args:
            name (str): The name of the member.
            birthdate (str): The birthdate of the member in YYYY-MM-DD.
            is_paid (bool): The payment status of the member.
            is_active (bool): The active status of the member, default is True.
            is_blocked (bool): The blocked status of the member, default is False.
        '''
        self.name = name
        self.birthdate = birthdate
        self.is_paid = is_paid
        self.is_active = is_active
        self.is_blocked = is_blocked
        Gym.members.append(self)
    def __str__(self):
        ''' Returns a string of the member's details. 
        Args:
            self: The class.
        '''
        return f'{self.name} | DOB : {self.birthdate} | Status : {"Paid" if self.is_paid else "Unpaid"}'
    @classmethod
    def show_members(cls, filter= None):
        ''' Displays all members or filters by paid/unpaid status. 
        Args:
            filter (str): "paid" or "unpaid" to filter members by payment status.
        '''
        # If no filter is provided, show all members
        # If filter is "unpaid", show only unpaid members
        # If filter is "paid", show only paid members
        for member in cls.members:
            if filter == "unpaid" and member.is_paid:
                # Skips Through loop if filter is "unpaid and member is paid"
                continue
            if filter == "paid" and not member.is_paid:
                # Skips Through loop if filter is "paid and member is unpaid"
                continue
            print(member)
    @classmethod
    def revoke_member(cls):
        ''' Revokes membership of a member based on their birthdate. 
        Args:
            cls: The class.
        '''
        date_of_birth = input("Please enter date of birth of member of who you would like to revoke memberhsip of (YYYY-MM-DD) : ")
        for member in cls.members:
            # Checks if the member's birthdate matches the input date
            if member.birthdate == date_of_birth:
                # If a match is found, it prompts for confirmation to revoke membership

                confirm = input(f'Are you sure you would like to revoke ({member}) membership? yes/no : ').lower()
                if confirm == 'yes':
                    # If confirmed, sets the members is_active status to False
                    member.is_active = False
                    print(f'You have revoked {member.name}s membership')
    @classmethod
    def block_members(cls):
        ''' Blocks all unpaid members.
        Args:
            cls: The class.
        '''
        # Prompts the user for confirmation before blocking all unpaid members
        confirm = input(f'Are you sure you would like to block all unpaid member? yes/no : ').lower()
        if confirm == "yes":
            # If confirmed, iterates through all members and sets is_blocked to True for unpaid members
            for member in cls.members:
                if member.is_paid == False:
                    member.is_blocked = True
            print(f'You have blocked all unpaid member')
    @classmethod
    def add_member(cls, name, birthdate, is_paid):
        ''' Adds a new member to the gym.
        
        Args:
            name (str): The name of the new member.
            birthdate (str): The birthdate of the new member.
            is_paid (bool): The payment status of the new member.
            cls: The class instance.
        '''
        # Creates a new Gym member instance and appends it to the members list
        cls(name, birthdate, is_paid)

    def convert_dict(self):
        ''' Converts the member to a dictionary.
        Returns:
            dict: A dictionary of the member's details.
        '''
        return {
            'name' : self.name,
            'birthdate' :self.birthdate,
            'is_paid' :self.is_paid,
            'is_active' :self.is_active,
            'is_blocked' :self.is_blocked
        }
    @classmethod
    def load_file(cls):
        ''' Loads members from a json file.
        Args:
            cls: The class.
        '''
        # Clears the existing members list before loading new data
        cls.members.clear()
        with open("gymapp/data/gym_members.json", "r") as f:
            members = json.load(f)
            for member in members:
                # Creates a new Gym member instance for each member in the json file
                member = cls(**member)
                cls.members.append(member)

    @classmethod
    def save_to_file(cls):
        ''' Saves members to a json file.
        
        Args:
            cls: The class.
        '''
        # Saves the current members list to a json file
        with open ("gymapp/data/gym_members.json", "w") as f:
            # Converts each member to a dictionary before saving
            json.dump([member.convert_dict() for member in cls.members], f, indent=4)

def add_new_member():
    '''
    This function prompts the user to input details for a new gym member and adds them to the gym.

    Args:
        None
    '''
    # Prompts the user for details of the new member
    name = input("Name of new member : ").casefold()        
    birthdate = input("Birthdate of new member (YYYY-MM-DD) : ")  
    paid_status = input("Has member paid? (Paid - Unpaid): ")
    # Converts the paid status input to a boolean value
    paid_status = True  if paid_status.lower() == "paid" else False
    # Adds the new member to the gym
    Gym.add_member(name, birthdate, paid_status)  
