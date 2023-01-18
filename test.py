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
   
    print('The aim of the game is to guess a word letter by letter\n')
    print('For each incorrect letter guess you will lose a life (7 in total) so choose carefully!\n')
    print('If you run out of lives and or complete a game you can restart by pressing either "Y" or "N" when prompted\n')

# def show_stats():
#     '''
#     Shows the status of your word
#     '''
#     global lives
#     os.system('clear')
#     print(hangman_lives(lives))
#     print(Fore.YELLOW + "You currently have",lives,"left!")


def generate_word():
    words = random.choice(word_choice)
    return words.upper()

def game_body(words):
    '''
    This function holds the majority of the functionality of hangman.
    from lives lost to letters being shown to the end game. To storing 
    guessed letters and number"
    '''
    lives = 6
    show_letter = '_' * len(words)
    guessed_letter = []
    guessed_word = []
    guess_complete = False
    title_intro()
    print(hangman_lives(lives))
    print(show_letter)
    print("\n")

    while not guess_complete and lives < 0:

        uguess = input(Fore.GREEN + "Please enter a letter!\n")

        if len(uguess) == 1 and uguess.isalpha():         
            if uguess in guessed_letter:
                print(Fore.RED + "You've already used", uguess, "! Be careful..")          
            elif uguess not in words:
                print(Fore.RED + uguess, "Is not in the word!")
                lives -= 1
                guessed_letter.append(uguess)        
            else:
                print(Fore.YELLOW + uguess, "is in the word! Keep it up!")
                guessed_letter.append(uguess)
                show_letter_list = list(show_letter)

                indicies = [i for i, letter in enumerate(show_letter)
                            if letter == uguess]
                for index in indicies:
                    show_letter_list[index] = uguess

                show_letter = "".join(show_letter_list)              
                if "_" not in show_letter:
                    guess_complete = True

        elif len(uguess) == len(words) and uguess.isalpha():        
            if uguess in guessed_word:
                print('You already guessed the word')          
            elif uguess != show_letter:
                print(Fore.RED + uguess, "Is not the word!")
                lives -= 1
                guessed_word.append(uguess)         
            else:
                guess_complete = True
                show_letter = words

        else:
            print(Fore.RED + "This is not a valid guess! Please try again...")

        print(hangman_lives(lives))
        print(show_letter)
        print("\n")
    if guess_complete:
        print(Fore.YELLOW + "Congrats you guessed the word and survived!")
    else:
        print(Fore.RED + gover)
        print(Fore.RED + "Word was", show_letter)

def show_stats(lives):
    '''
    Shows the status of your word
    '''
    for _ in stages:
        return stages[lives]



def main():
    '''
    Calls on all major functions
    '''
    # y_n_prompt = login.user_login()
    # login.c_login(y_n_prompt)
    words = generate_word()
    game_body(words)
    # while input("Would you like to plaay again? Y/N\n").upper() == "Y":
    #     words = generate_word()
    #     game_body(words)

if __name__  == "__main__":
    main()
