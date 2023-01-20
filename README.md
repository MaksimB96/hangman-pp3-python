# PP3 - Python Hangman
(Developer: Maksims Buraks)

![Mockup image](docs/intro-pic.png)

[live web-page](https://maksimb96.github.io/LoveBody/)

## Table of contents

1. [Project Goals](#project-goals)
    * [User Goals](#user-goals)
    * [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    * [Target Audience](#target-audience)
    * [User Requirements and Expectations](#user-requirements-and-expectations)
    * [User Stories](#user-stories)
3. [Design](#design)
    * [Design](#design-choices)
    * [Structure](#structure)
    * [Flow Chart](#flow-chart)
4. [Tech Used](#tech-used)
    * [Languages](#languages)
    * [Tools](#tools)
5. [Features](#features)
6. [Code Validation & Testing](#validation)
7. [Bugs](#bugs)
8. [Deployment](#deploy)
9. [Future Features](#future-features)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals
    -Finding a guess bassed game
    -To test guessing ability
    -To be able to return

### Site Owner Goals
    -Provide a simple and fun game 
    -Provide an area to login
    -Provide the option to restart

## User Experience

### Target Audience
    -People looking to test guess ability

### User Requirements and Expectations
    -A simple and intuative design
    -Quick inputs without complication
    -Clear visual markers on each turn
    -A way to restart

### User Stories

#### First-time User
1. As a first time user, I want to play hangman
2. As a first time user, I want to test my guessing skills
3. As a first time user, I want a simple and intuative interface
4. As a first time user, I want to have the option to restart

#### Returning User
5. As a returning user I want to login and play again
6. As a returning user I want to see diferent word sets
7. As a returning user I want to be able to play again

#### Site Owner
8. As a site owner I want people to be able to login and play
9. As a site owner I want people to be able create an account  
10. As a site owner I want people to either play again or not

## Design

### Design Choices
The game while being run in a terminal has some ascii art and terminal text colour in order to make it pop and be less monotone.

### Structure
The stucture while being relativly basic, is intuative. You are greeted with a login segment, the main game body and then a prompt to restart. If yes the loop begins again, if no, you are greeted with 'farewell' art and then retun to the login portion of hangman.

<br>

The game is made up of 3 stages:

    -Login: Tests if you aree new or an old user 
    -The main game body
    -Restart: If yes, then game loops if no, then return to login

### Flow Chart
<details><summary>Main Flow-Chart</summary>
<img src="docs/flowchart/flow.jpeg">
</details>

-Blue is the login flow, red is the main game body, yellow are choices.

## Tech Used

### Languages
    -Python

### Tools
    -Git
    -Git Hub
    -Git Pod
    -Lucid-Chart
    -Heroku
    -Ascii art generator
    -random word generator
    -PEP8 CI Python Linter

## Features
The Game consists of 3 segments each with their own features

### Login
    -Greeted to hangman and option if you are either a old/new user 
    -If you are new, you enter details (password/username) that get written on spreeadsheet
    -If you are a old user, you enter existing information
    -If either username or password incorrect error will be thrown and login will begin again.
    -once details entered main title intro will play, that is slowed with sleep function
    -User Stories adressed: 3, 5, 8, 9
    
![Login](docs/features/correct-user.png)
<br>

![Login](docs/features/password-wrong.png)
<br>

![Login](docs/features/wrong-user.png)

![Login](docs/features/usernames.png)

![Login](docs/features/passwords.png)

![Login](docs/features/title.png)


### Game Body
    -After title intro has played, users will be presented with the main game phase
    -Clear screen function focuses on the hangman game
    -Correct inputs show on empty guess word
    -Incorrect guesses provide feedback and increments the hangman
    -Inputs greater than one will throw error
    -If all lives exhausted leads to game over
    -If guess is correct, you win!
    -User stories adressed: 1, 2, 3, 6

![Game Body features](docs/features/title.png)
![Game Body features](docs/features/enter-letter.png)
![Game Body features](docs/features/incorrect-hm-input.png)
![Game Body features](docs/features/incorrect-lives.png)
![Game Body features](docs/features/correct-reveal.png)
![Game Body features](docs/features/gameover-loop.png)
![Game Body features](docs/features/win.png)



### Restart
    -After loss or win you ar prompted with a restart
    -Checks against valid input
    -If yes, you restart game, if no you get a goodbye message and go back to login
    -User stories adressed: 4, 7, 10

![Restart Seg](docs/features/gameover-loop.png)
![Restart Seg](docs/features/win.png)

## Validation

### PEP8 - CI Python Linter
PEP8 - CI Python Linter, was used in order to validate my code for my login.py code and run.py code. Rand-words and hangman-titles were not included as they
only focused being called as art or to grab a random words.

<details><summary>Game Body</summary>
<img src="docs/validations/test-run.png">
</details>
<details><summary>Login</summary>
<img src="docs/validations/test-login.png">
</details>

<br>



### Tests

#### Error Test:
    -Tested multitude of inputs for Login
    -Tested multitude of inputs for Game Body
    -Tested multitude of inputs for Restart


### Testing User Stories

1. As a first time user, I want to play hangman
2. As a first time user, I want to test my guessing skills
3. As a first time user, I want a simple and intuative interface
4. As a first time user, I want to have the option to restart
5. As a returning user I want to login and play again
6. As a returning user I want to see diferent word sets
7. As a returning user I want to be able to play again
8. As a site owner I want people to be able to login and play
9. As a site owner I want people to be able create an account  
10. As a site owner I want people to either play again or not



<br>

| **Feature** | **Action** | **Expected Results** | **Final Result** |
|-------------|------------|----------------------|------------------|
|             |            |                      |                  |
| Home page, Linked Icons| Burger Menu/ Desktop menu show relevant info, icons link to poi's| Interactive Elements prompt to trravel to relevant poi's| Home page prompts user to travel to all locations from home page|
|Quiz| Allows user to test knowledge in relation to fitness| Clear visual indicators for correct/wrong answer, questions cycle and then reset as intended|Quiz Works as intended|
|Feedback Form| Input fields only submit once form validated| Form validates inputs and sends feedback to me| Form Works as intended|

<br>

| **Feature** | **Action** | **Expected Results** | **Final Result** |
|-------------|------------|----------------------|------------------|
|             |            |                      |                  |
|Restart Prompt|User has y/n option| either restart or exit game back to login| Works as intended|

<br>

## Bugs

| **Bug** | **Fix** | 
|---------|---------|
|         |         | 
|Restart Scores did not work as intended| Created new button instead of changing inner html and defind it, and added functions that reset score on click via event listener|
|Form not validating|Added correct string in order validate |
|Initial break of quiz| Corrected elements by id and programmed restart button and function correctly|

## Deployment

Deployment of site was acheived through these steps:
1. I navigated to the settings section on git hub repositories on my repository.
2. I then selected the pages link on the left side.
3. I then selected source for the branch prompt.
4. Roughly, 2 minutes after refreshing I recieved a link to my site: https://maksimb96.github.io/LoveBody/ 

## Future Features

There are a few more feartures that I would like to implement in the future. These Include:
1.Polished Nav Bar with smooth transition
2.Timer function to quiz
3.Randomize the order of how button answers display
4.A progress Bar to track progress

## Credits

### Media

All media created by me using  <a href="https://www.canva.com/">Canva</a>, this includes Icons and backgound images.
<br>
Any Icons used found on <a href="https://fontawesome.com/">Font Awesome</a>
<br>
Burger Image by <a href="https://www.flaticon.com/free-icon/menu_4254068?term=menu-burger&page=1&position=2&page=1&position=2&related_id=4254068&origin=tag#">Andy Horvath</a>
<br>
X Image by <a href="https://www.flaticon.com/free-icon/close_2997911?term=x&page=1&position=5&page=1&position=5&related_id=2997911&origin=tag# ">Fuzzee</a>
    
### Code 

1. 404 page code provided by Mo Shami_mentor from code institue
2. favicon idea provided by Mo Shami_mentor, site used found <a href="https://favicon.io/"> here</a>
3. Form Validation inspiraation by <a href="https://www.youtube.com/watch?v=fz8bwvn9lA4"> Easy Tutorials</a>
4. Increment of answers inspired by LoveMaths by Code Institute
5. Text shadow property taken from <a href="https://www.w3schools.com/cssref/css3_pr_text-shadow.php"> w3schools</a>
6. Email Validation strings by <a href="https://www.w3resource.com/javascript/form/email-validation.php">W3Schools</a>
7. Burger Nav bar help from tutor support
8. Reset button functionality help from tutor support
9. EmailJs instructions may be found on <a href="https://www.emailjs.com/">EmailJS</a>
10. Quiz inspiration taken from  <a href="https://www.youtube.com/watch?v=riDzcEQbX6k">Web Dev Simplified</a>


## Acknowledgements

-I would like to thank Victor my mentor or providing aamazing feedback!
<br>
-CI for provide me the knowledge to under-take this task specifically python module and love sandwiches
<br>
-Tutor Support for provideing better knowledge to implement the code and help me see minor errors
<br>
-My beautiful girlfriend who added literally one quetion mark
<br>
-The wonderful community over on Slack!











