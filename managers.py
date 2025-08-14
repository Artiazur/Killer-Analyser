import os
from colorama import init, Fore, Style, Back
init(autoreset=True)
from validation import Validator


class UsernameManager:
    @staticmethod
    def check_user_name_exists():
        if os.path.exists("user_name.txt"):
            with open("user_name.txt", "r") as file:
                user_name = file.read()
                return user_name
        else:
            with open("user_name.txt", "w") as file:
                MessagesManager.first_message()
                user_name = InputManager.get_user_name()
                file.write(user_name)
                MessagesManager.save_user_name(user_name)
                return user_name


class InputManager:
    @staticmethod
    def get_user_name():
            user_name = input(MessagesManager.get_user_name_message())
            return user_name

    @staticmethod
    def ask_ready(user_name):
        while True:
            choice = input(MessagesManager.ask_ready_message(user_name))
            if choice :
                if Validator.is_yes_or_no(choice):
                    return choice
                else:
                    ErrorManager.invalid_input()
            else: 
                ErrorManager.empty_input()
                
    @staticmethod
    def ask_exit(user_name):
        while True:
            choice = input(MessagesManager.ask_exit_message(user_name))
            if choice:
                if Validator.is_yes_or_no(choice):
                    return choice
                else:
                    ErrorManager.invalid_input()
            else:
                ErrorManager.empty_input()
                
    @staticmethod
    def back_to_main_menu(user_name):
        while True:
            choice = input(MessagesManager.ask_exit_message(user_name))
            if choice:
                if Validator.is_yes_or_no(choice):
                    return choice
                else:
                    ErrorManager.invalid_input()
            else:
                ErrorManager.empty_input()

    @staticmethod
    def get_menu_options(user_name):
         while True:
            choice = input(MessagesManager.menu_option_message(user_name))
            if choice:
                if Validator.is_choice(choice):
                    return choice
                else:
                    ErrorManager.invalid_input()
            else:
                ErrorManager.empty_input()
        

class MessagesManager:
    @staticmethod
    def first_message():
        print(f"{Fore.RED}{Style.BRIGHT}Hi! I'm sure you're really curious about {Back.WHITE}murder and serial killers!{Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}\nso let's start this journey together.")

    @staticmethod
    def save_user_name(user_name):
        print(f"{Style.BRIGHT}{Fore.RED}\n***Dear {user_name} your name has been saved.***{Style.RESET_ALL}")

    @staticmethod
    def wellcome_message(user_name):
        print(f"""
        {Style.BRIGHT}{Fore.RED}Hi {user_name}! Welcome to a dark, real, and mysterious journey…
        Did you know that over 400 murders happen every single day around the world?
        And did you know that some of those killers are still living freely among us?
        Or that most serial killers aren’t insane or mentally ill but intelligent?
        Or that some killers choose their victims solely based on hair color or gender?
        The world is full of unsolved cases…
        Full of questions that remain unanswered…
        Full of people who thought, “That could never happen to me.”
        If you have a curious mind and aren’t afraid to face the darkest corners of reality...
        Then come along and start this journey with me.
        """)

    @staticmethod
    def get_user_name_message():
        return (f"{Fore.RED}{Style.BRIGHT}\nPlease enter your name: ")

    @staticmethod
    def ask_ready_message(user_name):
        return (f"{Fore.RED}{Style.BRIGHT}Dear {user_name}, are you ready to start? (yes/no): ")

    @staticmethod
    def ask_exit_message(user_name):
        return (f"{Fore.RED}{Style.BRIGHT}Dear {user_name}, do you want to leave the app? (yes/no): ")

    @staticmethod
    def back_to_main_menu_message(user_name):
        return (f"{Fore.RED}{Style.BRIGHT}Dear {user_name}, do you want to return to main menu? (yes/no):  ")

    @staticmethod
    def menu_option_message(user_name):
        return (f"{Fore.RED}{Style.BRIGHT}Dear {user_name}, what do you want to do?:  ")
    
    @staticmethod
    def show_corr():
        return(f"{Fore.RED}{Style.BRIGHT}Correlation between duration and victims:")

    @staticmethod
    def positive_corr():
      return(f"{Fore.RED}{Style.BRIGHT}Positive correlation: Longer active years tend to mean more victims.")
  
    @staticmethod
    def negative_corr():
      return(f"{Fore.RED}{Style.BRIGHT}Negative correlation: Longer active years tend to mean fewer victims.")
    
    @staticmethod
    def no_corr():
      return(f"{Fore.RED}{Style.BRIGHT}No significant correlation between active years and victims.")  
  
    @staticmethod
    def country_crime_result(safest_country, most_dangerous_country):
        print(
            f"{Fore.GREEN}{Style.BRIGHT}\nThe safest country is: \n{safest_country}",
            f"{Fore.RED}{Style.BRIGHT}The Most dangerous country is: \n{most_dangerous_country}",
            sep="\n" * 2
              )  


class ErrorManager:
    @staticmethod
    def empty_input():
        print(
            f"{Fore.YELLOW}{Style.BRIGHT} ERROR! Input cannot be empty.{Style.RESET_ALL}")

    def invalid_input():
        print(f"{Fore.YELLOW}{Style.BRIGHT} ERROR!Input is not Valid. Please enter 'yes' or 'no'.{Style.RESET_ALL}")
