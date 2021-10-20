# JPT-96-MSProject3(Black Jack)-Resubmission

## About
For my Python project I decided to go with a very simple version of black Jack game.

![loadingscreen](images/loadingscreen.png)

[click here](https://jpt-96-blackjack-resubmission.herokuapp.com/) to see deployed game.

## Contents


1. [Project Goals](#project-goals)
2. [User Goals](#user-goals)
3. [Features](#features)
4. [Structure](#structure)
    1. [Home Screen](#home-screen)
    2. [place bet](#place-bet)
    3. [Hit or Hold](#hit-hold)
    4. [end game result](#end-game-result)
5. [Design](#design)
6. [Function Purposes](#function-purposes)
7. [user stories](#user-stories)
8. [technologies Used](#technologies-used)
9. [testing](#testing)
10. [future features](#future-features)
11. [deployment](#depolyment)


## Project Goals
my project goals are:
- create a BlackJack game that is easy to use.
- to take a gamble input
- to have readable cards
- a easy to follow score system


## User Goals
my user goals are:
- easy instructions if player doesn't follow the steps
- to have a basic understanding of Python


## Features
This game has cards and a simple hit or hold function and will keep going till you hit 21.
It has some fun print statements in it to give the player something more interesting to look at rather than just "Dealer wins" or "Player wins".
It also now has a error message if hit or hold isn't entered to remind the user of what is required with a reminder that capitalisation is also required.

## Structure
The structure of this BlackJack game relys on user inputs in order to work.

### 1. Home Screen
<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of Home screen](images/loadingscreen.png)

</details>
This is Home/loading screen. It has a simple welcome message and a prompt to enter a gambling bet.

### 2. Place Bet
<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of taking bet](images/gamble.png)

</details>
This shows that a input has been made for the amount of chips the user is betting.

### 3. Hit or Hold
<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of taking bet](images/hit.png)

</details>
This shows another card is printed when Hit is inputed into the console.

### 4. End Game result

<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of taking bet](images/endgame.png)

</details>

This shows the end result of a turn.




## Design
The design of the cards is used with print statements using | and - to for the bases of a card whilst calling f prints to print the value of said card.

### Function Purposes 
In this sub section I would like to go over my functions and give a breif run down of what they do and the objective that they achieve.
This will show my thought process and even help others that wish to do a similar project.
## Import
So first thing you need to do is import random. This is very important because you need the deck to be shuffled and distributed randomly this allows for a fair game.
## Functions & Classes
### card
This first function is called card.
This is essentially comprised of a list with the values of the cards which get reassinged in the print statements. In order to create the cards
underneath this we give the __init__ within  this class, we then assign self to all neccessary variables. 
After this we then define the value of the cards with things like >= 10 for example.

### deck
We create an empty list that has the self.cards.
In here we begin with creating the actual deck by generating 52 cards and create 4 suits of each.
After this we then append it to the card using the I and J used to create the 52 cards and the different suits.
### Draw
Inside the draw function we are simply itterating and appending to the self.cards which is defined later on.
As well as appending to the card we defined earlier, when this is done at the end we return cards (not card see what I mean about naming conventions)
.
### count 
This is one line of code that reads the length of the self.cards.

### player and dealer
Within this class we essentially are assigning cards as a empty list, dealer = dealer score= 0 etc etc.
From here we create the deal and hit functions. This is essentially checking if the score equats to 21 and if the player
wants to hit, if so then we extend the hand essentially by adding another card. 
After this we do our ace alteration, by essentially saying if score is over 21 we assign it the value of 1 else it is a 11.
Once the score hit's 21 we reveal the cards of both players. We also later down the line figure out if the dealer or player has 21. 


### the game 
In here is where we essentially put in the rules. What it takes to bust what it takes to win which is having a higher score but not over 21.
I also put in a way if the dealer has under 17 the dealer should hit as it is highly unlikely it will bust making the game a bit more competitve.
We then reveal both players cards when the player is happy and the dealer is over 17. We then compare results and add appropriate print statements.
I then iniate the game by going b = the_game b.round() which is a function defined earlier in the code

This is a very basic run through of the functions and classes but gives you some idea of my thought process and approach towards this project.



## Future Features
I would like to add currency (not real) to make it feel like your gambling for more immersion in this game. I also would like to do a couple of turns in this project,  
that would allow the player to get a couple of rounds in and fully enjoy this project.


## Technologies used
### Languages used
[python3](https://en.wikipedia.org/wiki/Python_(programming_language) This was only a python3 project.

### apps and platforms
[Heroku](https://www.heroku.com) this is used to deploy the app for free
[Gitpod](https://gitpod.com/) this is where all the code was written
[Github](https://github.com/) This is where all of my project repos exist and are hosted.
[Git](https://git-scm.com/)  This is a control system that allows me to push commits and changes to github/gitpod
 
## Testing
The majority of the testing is done through the terminal in VS code and gitpod.
There were a few bugs with previous itterations of this project which you will find within the comments made, using things such as classes and __init__ 
as an example. But I ran into a lot of errors that I didn't know how to fix so I reverted back to a very basic version. 
My naming convetions could of been cleaner there are some basic issues like naming functions very similarly for example price and cost are too similiar.
Which actually caused the project to not work for a day or two because I couldn't understand the errors that were occuring.
When graded it was apparent that there was no error handling so now there is a error message that will display if Hit or Hold isn't entered.
This is to remind you of what is required in order to procceed with the game.


## Deployment 
### Publishing
 1. Go to the GitHub website and log in.
 2. On the left-hand side, you'll see all your repositories, select the appropriate one. (Repository used for this project).
 3. Under the name of your chosen Repository you will see a ribbon of selections, click on 'Settings' located on the right hand side.
 4. Scroll down till you see 'GitHub Pages' heading. 
 5. Under the 'Source' click on the dropdown and select 'master branch' 
 6. The page will reload and you'll see the link of your published page displayed under 'GitHub' pages. 
 7. It takes a few minutes for the site to be published, wait until the background of your link changes to a green color before trying to open it.
 
