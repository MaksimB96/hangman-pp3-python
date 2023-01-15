import colorama
import random
from colorama import Fore
from hangman_titles import title

colorama.init(autoreset = True)

def title_intro():
    '''
    Intro art and basic run down of how to play
    '''

    print(Fore.GREEN + title)
    print('Welcome to hangman!')
    
