# imports to access my sheet
import random
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back

# Love sandwiches inspired code
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p_users')


def user_login() -> str:
    """
    This function will help determine if a user is new or returning
    If new, the user will be set up, otherwise a login will be asked
    """
    while True:
        print(Fore.BLUE + '~~~~~~~~~~~~~~~~~~~')
        print(Fore.BLUE + 'Welcome to Hangman!')
        print(Fore.BLUE + '~~~~~~~~~~~~~~~~~~~')
        y_n_prompt = input("Are you a new user? Y/N\n").lower()

        if str(y_n_prompt) == "y":
            newu()
        elif str(y_n_prompt) == "n":
            oldu()

        if c_login(y_n_prompt):
            break

    return y_n_prompt


def c_login(y_n_prompt: str):
    """
    Checks if user inputs are correct. If not Errors will be raised
    Specifically Value Error
    """
    try:
        str(y_n_prompt)
        if y_n_prompt not in {"y", "n"}:
            raise ValueError(Fore.RED + "That Input is incorrect")

    except ValueError as e:
        print(Fore.RED + f"{e} Please enter either Y or N")
        return False

    return True


def newu():
    """
    If the user is new, password and name will be required to enter,
    then will be stored on google spreadsheet
    """
    # New user segment
    new_user_log = SHEET.worksheet("users")
    new_user_pass = SHEET.worksheet("passwords")
    new_user_in = input(Fore.BLUE + "Please enter a username\n")
    user_list = str.split(new_user_in)
    new_user_log.append_row(user_list)
    print(Fore.YELLOW + f"Welcome {new_user_in}")

    # Password segment
    new_pass_in = input(Fore.BLUE + "Please enter a password\n")
    pass_list = str.split(new_pass_in)
    new_user_pass.append_row(pass_list)
    print(Fore.YELLOW + "Password Saved! Enjoy the game!")


def oldu():
    """
    If user is returning, They will be prompted to enter their details
    that they previously have inputed if they were a new user. If The
    info provided is false, they'll need to restart.
    """
    new_user_log = SHEET.worksheet("users")
    new_user_pass = SHEET.worksheet("passwords")

    # Old username prompt
    old_user_in = input("Please enter your username\n")
    info_check_name = new_user_log.find(old_user_in)

    # If username not found user login function will be called
    if info_check_name is None:
        print(Fore.RED + "This username does not exist! Please try again...")
        user_login()
    else:
        print(Fore.YELLOW + f"Welcome back {old_user_in}!")

    # Password segment for returning users
    old_pass_in = input("Please enter your password\n")
    info_check_pass = new_user_pass.find(old_pass_in)

    # If password not found user login function will be called
    if info_check_pass is None:
        print(Fore.RED + "Password incorrect! Please try again...")
        user_login()
    else:
        print(Fore.YELLOW + "Password is correct! Enjoy the game!")
