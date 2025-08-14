import os

class Validator:
    @staticmethod
    def is_yes_or_no(user_input : str, empty=False):
        if user_input.strip().casefold()[0] == "y":
                return True
        elif user_input.strip().casefold()[0] == "n":
                return True
        
        
    @staticmethod
    def is_choice(menu_choice):
        pattern = "1234"   
        if menu_choice in pattern:
            return True
        else:
            return False
