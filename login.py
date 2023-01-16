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



    
