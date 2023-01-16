import colorama
import gspread
import random
from colorama import Fore
from google.oauth2.service_account import Credentials
from hangman_titles import title

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p_users')

username = SHEET.worksheet('pw')

print(username)
# colorama.init(autoreset = True)

# def title_intro():
#     '''
#     Intro art and basic run down of how to play
#     '''

#     print(Fore.GREEN + title)
#     print('Welcome to hangman!')

