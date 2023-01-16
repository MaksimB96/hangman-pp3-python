#imports to access my sheet
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore, Back

#Love sandwiches inspired code
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
        print(Fore.BLUE + '~~~~~~~~~~~~~~~~~~~~~')
        print('Welcome to Hangman!')
        print(Fore.BLUE + '~~~~~~~~~~~~~~~~~~~~~')
        y_n_prompt = input(Back.GREEN + "Are you a new user? Y/N").lower()

        if str(y_n_prompt) == y:
            newu()
        elif str(y_n_prompt) == n:
            oldu()

        if c_login(y_n_prompt):
            break
        return y_n_prompt

def c_login():
    """
    Checks if user inputs are correct. If not Errors will be raised
    Specifically Value Error
    """
    try:
        str(y_n_prompt)
        if y_n_prompt not in {"y", "n"}:
            raise ValueError(Fore.RED + "That Input is incorrect")
    except ValueError as e:
        print(f"{e} Please enter either Y or N")
        return False
    return True


def newu():
    """
    If the user is new, password and name will be required to enter,
    then will be stored on google spreadsheet
    """
    #New user segment
    new_user_log = SHEET.worksheet("user")
    new_user_pass = SHEET.worksheet("passwords")
    new_user_in = input(Fore.BLUE + "Please enter a username\n")
    user_list = str.split(new_user_in)
    new_user_log.append_row(user_list)
    print(Fore.YELLOW + f"Welcome {new_user_in}")

    #Password segment
    new_pass_in = input(Fore.BLUE + "Please enter a password\n")
    pass_list = str.split(new_pass_in)
    new_user_pass.append_row(pass_list)
    print(FORE.YELLOW + "Password Saved!")




def oldu():


    
