import colorama
import random
from colorama import Fore
from hangman_titles import title, gbye, gover, lives_list

colorama.init(autoreset = True)

def title_intro():
    '''
    Intro art and basic run down of how to play
    '''

    print(Fore.GREEN + title)
    print('Welcome to hangman!\n')
    print('The aim of the game is to guess a word letter by letter\n')
    print('For each incorrect letter guess you will lose a life (7 in total) so choose carefully!\n')
    print('If you run out of lives and or complete a game you can restart by pressing either "Y" or "N" when prompted\n')

title_intro()


