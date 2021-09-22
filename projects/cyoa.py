"""Fun Fair Adventure !"""

__author__ = "730391424"
from random import randint
FERRIS_WHEEL: str = "\U0001F3A1"
ROLLER_COASTER: str = "\U0001F3A2" 
THINK_FACE: str = "\U0001F914"

points: int = 0
player: str = ""


def greet() -> None:
    """Greet and welcome the player."""
    print("Hello! Welcome to our fun fair! In this game you will decide which parts of the fair to explore and earn points as you make your choices! \U0001F3A1\U0001F3A2")
    global player
    player = str = input("Before we begin (and for 5 starter points), what is your name? ")
    print(f"Welcome to the game, {player}") 
    global points
    points = points + 5


def main() -> None:
    greet()
    points: int = 0 
    path: str = input(f"{player}, would you like to... one: Ride the Ferris Wheel. two: Go to the Tarot Card Booth. three: Get funnel cake. or four: Quit game. Type the option you are selecting in lowercase with no spaces or colons please! ")
    if path == "one":
        ferris_wheel()
    if path == "two":
        tarot()
    if path == "three":
        funnel_cake()
    if path == "four":
        print(f"Goodbye {player}! Thank you so much for playing! You earned {points} points! Amazing job!")


def ferris_wheel():


def funnel_cake():


def tarot(): 
    print("You picked the ...")
    SECRET: int = int(randint(1, 4))
    if SECRET == 1: 
        print("Star Tarot Card! This card has to do with cosmic protection!")
    else: 
        if SECRET == 2: 
            print("Ace of Pentacles Tarot Card! This card means you will win!")
        else: 
            if SECRET == 3: 
                print("Four of Wands Tarot Card! This card has to do with success and joy!")
            else: 
                if SECRET == 4: 
                    print("The Sun Tarot Card! This card relates to joy, happiness, and triumph!")
    print(f"Hmmm,{player} I wonder what that could mean for you. \U0001F914")


# def main() -> None: 
if __name__ == "__main__":
    main()

# I received the tarot card information from https://www.tarotparlor.com/blog/most-positive-tarot-cards