#colorama used for more color variation 
import colorama

#random and os used for random functionality and os for clear screen 
import random, os, time

#login.py imported for user integration
import login

#gspread used for spreadsheet data handling
import gspread

#rand-word.py list imported to be utilised in game
from rand_word import word_choice

#imported specific aspects for data handle, color and titles
from google.oauth2.service_account import Credentials
from colorama import Fore
from time import sleep
from hangman_titles import title, gbye, gover, stages

#scope used for data handling - credit love sandwich
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json') 
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p_users')

#colorama init used as per colorama manual - see readme
colorama.init(autoreset = True)

def title_intro():
    '''
    Intro art and basic run down of how to play
    '''
    print(Fore.LIGHTGREEN_EX + title)
    sleep(1.3)
    print('The aim of the game is to guess a word letter by letter\n')
    sleep(1.3)
    print('For each incorrect letter guess you will lose a life (7 in total) so choose carefully!\n')
    sleep(1.3)
    print('If you run out of lives and or complete a game you can restart by pressing either "Y" or "N" when prompted\n')
    sleep(1.3)
    reset_screen()

def generate_word():
    words = random.choice(word_choice)
    return words.upper()

def game_body(words):
    '''
    This function holds the majority of the functionality of hangman.
    from lives lost to letters being shown to the end game. To storing 
    guessed letters and number"
    '''
    lives = 7
    show_letter = '_' * len(words)
    guessed_letter = []
    guess_complete = False
    print(show_stats(lives))
    print(Fore.YELLOW + "You currently have",lives, Fore.YELLOW+"lives left!\n")
    print(show_letter)
    print("\n")

    while not guess_complete and lives > 0:
        uguess = input("Please enter a letter!\n").upper()

        if len(uguess) == 1 and uguess.isalpha():         
            
            if uguess in guessed_letter:
                reset_screen()
                print(Fore.RED + "You've already used", uguess)
            elif uguess not in words:
                reset_screen()
                print(Fore.RED + uguess, "Is not in the word!")
                lives -= 1
                print(Fore.YELLOW + "You currently have",lives, Fore.YELLOW+"lives left!\n")
                guessed_letter.append(uguess)        
            else:
                reset_screen()
                print(Fore.YELLOW + uguess, "is in the word! Keep it up!")
                print(Fore.YELLOW + "You currently have",lives,"left!\n")
                guessed_letter.append(uguess)
                show_stats(lives)
                show_letter_list = list(show_letter)
                indicies = [i for i, letter in enumerate(show_letter) if letter == uguess]
                for index in indicies:
                    show_letter_list[index] = uguess
                show_letter = "".join(show_letter_list)              
                if "_" not in show_letter:
                    guess_complete = True
        
        elif len(uguess) == len(words) and uguess.isalpha():                 
            
            if uguess != show_letter:
                reset_screen()
                print(Fore.RED + uguess, "Is not the word!")
                lives -= 1
            else:
                guess_complete = True
                show_letter = words
        else:
            reset_screen()
            print(Fore.RED + "This is not a valid guess! Please try again...")
        
        print(show_stats(lives))
        print(show_letter)
        print("\n")

    if guess_complete:
        reset_screen()
        print(Fore.YELLOW + "Congrats you guessed the word and survived!")
    else:
        reset_screen()
        print(Fore.RED + gover)
        print(Fore.RED + "Word was", words)

def show_stats(lives):
    '''
    Shows the status of hangman, that returns when lives exhausted
    '''
    for _ in stages:
        return stages[lives]


def reset_screen():
    '''
    Basic function that clears the screen after each turn, this makes UI
    cleaner
    '''
    os.system('clear')

def game_restart() -> str:
    while True:
        restart_prompt = input("Would you like to play again?").upper()
        if restart_prompt == "Y":
            reset_screen()
            words = generate_word()
            game_body(words)
        elif restart_prompt == "N":
            reset_screen()
            print(Fore.LIGHTGREEN_EX + gbye)

    

def main():
#     '''
#     Calls on all major functions
#     '''
#     # y_n_prompt = login.user_login()
#     # login.c_login(y_n_prompt)
    title_intro()
    words = generate_word()
    game_body(words)


if __name__== "__main__":
    main()
