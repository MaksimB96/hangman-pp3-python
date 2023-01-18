#colorama used for more color variation 
import colorama

#random and os used for random functionality and os for clear screen 
import random, os

#login.py imported for user integration
import login

#gspread used for spreadsheet data handling
import gspread

#rand-word.py list imported to be utilised in game
from rand_word import word_choice

#imported specific aspects for data handle, color and titles
from google.oauth2.service_account import Credentials
from colorama import Fore
from hangman_titles import title, gbye, gover

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
   
    print('The aim of the game is to guess a word letter by letter\n')
    print('For each incorrect letter guess you will lose a life (7 in total) so choose carefully!\n')
    print('If you run out of lives and or complete a game you can restart by pressing either "Y" or "N" when prompted\n')


def generate_word():
    choices = random.choice(word_choice).upper()
    return choices

def game_body(choices):
    '''
    This function holds the majority of the functionality of hangman.
    from lives lost to letters being shown to the end game. To storing 
    guessed letters and number"
    '''
    lives = 7
    show = list(len(choices)*'_')
    guessed_letter = []
    guessed_word = []
    game_complete = False
    title_intro()
    print(hangman_lives_dict(lives))
    print(show)
    print("\n")

    while game_complete == False and lives > 0:
        
        uguess = input(Fore.GREEN + "Please enter a letter!\n")
        uguess = uguess.upper()
        if len(uguess) == 1 and uguess.isalpha():
            
            if uguess in guessed_letter:
                print(Fore.RED + "You've already used",uguess,"! Be careful..")
            
            elif uguess not in choices:
                print(Fore.RED + uguess, "Is not in the word!")
                lives -= 1
                guessed_letter.append(uguess)
            
            else:
                print(Fore.YELLOW + uguess, "is in the word! Keep it up!")
                guessed_letter.append(uguess)
                show_in_list = list(show)
                indicies = [i for i, letter in enumerate(choices) if letter == uguess]

                for index in indicies:
                    show_in_list[index] = uguess
                show = "".join(show_in_list)
                
                if "_" not in show:
                    game_complete = True

        elif len(uguess) == len(choices) and uguess.isalpha():
            
            if uguess in guessed_word:
                print('You already guessed the word')
            
            elif uguess != choices:
                print(Fore.RED + uguess, "Is not the word!")
                lives -= 1
                guessed_word.append(uguess)
            else:
                game_complete = True
                show = choices
        else:
            print(Fore.RED + "This is not a valid guess! Please try again...")
            print(show)
            print(hangman_lives_dict(lives))
    
    if game_complete:
        print(Fore.YELLOW + "Congrats you guessed the word and survived!")
    else:
        print(Fore.RED + gover)
        print(Fore.RED + "Word was",choices)

def hangman_lives_dict(lives):
    hangman_lives =[
"""
    +---+
        |
        |
        |
        |
        |
=========
""",
"""
    +---+
    |   |
        |
        |
        |
        |
=========
    """,
"""
    +---+
    |   |
    O   |
        |
        |
        |
=========
    """,
"""
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
    """,
"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
    """,
"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
    """,
"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========
    """,
"""
    +---+
    |   |
   *_*  |
   /|\  |
   / \  |
        |
=========
 """
]

# def game_restart():
#     '''
#     Allows user to restart the game 
#     '''

        

def main():
    '''
    Calls on all major functions
    '''
    y_n_prompt = login.user_login()
    login.c_login(y_n_prompt)
    choices = generate_word()
    game_body(choices)
    while input(Fore.GREEN + "Would you like to play again? Y/N\n").upper() == "y":
        choices = generate_word()
        game_body(choices)


    

main()


    #     if uguess == choices:
    #         game_complete = True
    #         show = choices
    #     if len(uguess) == 1 and uguess in choices:
    #         game_complete = c_letter(uguess, choices)

    #     else:
    #         lives -= 1
    #     show_stats()

    # if game_complete:
    #     print(Fore.YELLOW + "Congratulations, your guessing skills are most impressive")
    # else:
    #     print(Fore.RED + gover)
    #     print(Fore.RED + "The word was:", choices)










# def main():
#     '''
#     Calls on all major functions
#     '''
#     y_n_prompt = login.user_login()
#     login.c_login(y_n_prompt)
#     title_intro()
#     game_body(choices)
    

# main()
