import colorama
import random
import login
import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore
from hangman_titles import title, gbye, gover, lives_list

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p_users')

colorama.init(autoreset = True)

def title_intro():
    '''
    Intro art and basic run down of how to play
    '''

    print(Fore.GREEN + title)
   
    print('The aim of the game is to guess a word letter by letter\n')
    print('For each incorrect letter guess you will lose a life (7 in total) so choose carefully!\n')
    print('If you run out of lives and or complete a game you can restart by pressing either "Y" or "N" when prompted\n')


def main():
    y_n_prompt = login.user_login()
    login.c_login(y_n_prompt)
    title_intro()
    

main()
