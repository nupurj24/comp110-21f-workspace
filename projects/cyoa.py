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
    player = input("Before we begin, what is your name? ")
    print(f"Welcome to the game, {player}!") 


def ferris_wheel() -> int:
    """Ferris Wheel Choices"""
    global points 
    print(f"Welcome to the Ferris Wheel ride, {player}! Unfortunately, there is a line for this ride for 30 minutes.")
    choice: str = input(f"{player}, Would you like to... one: Wait in line for the ride. or two: choose another option? Type the option you are selecting in lowercase with no spaces or colons please! ")
    if choice == "one":
        print(f"The wait was worth it! We hope you enjoyed the view, {player}!")
        points = points + 20
    else: 
        if choice == "two":
            print(f"That makes sense, {player}! Time is of the essence!")
            points = points + 5
    return points


def tarot() -> int:
    """Tarot Card Booth"""
    print("You picked the ... ")
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
    print(f"Hmmm, {player} I wonder what that could mean for you. \U0001F914")
    global points
    points = points + 10
    return points


def funnel_cake(points: int) -> int:
    """Funnel Cake Stand"""
    funnel_points: int = 0
    bogo: str = input(f"Good News! You received a buy one get one free funnel cake coupon upon your ticket purchase, {player}! Would you like to... one: Keep the free funnel cake for yourself. or two: Give it to the person in line behind you. Type the option you are selecting in lowercase with no spaces or colons please! ")
    if bogo == "one":
        funnel_points = funnel_points + 5
    else: 
        if bogo == "two":
            funnel_points = funnel_points + 30
    return funnel_points


def main() -> None:
    greet()
    global points
    points = 0 
    path: str = ""
    while path != "four":
        path = input(f"{player}, would you like to... one: Ride the Ferris Wheel. two: Go to the Tarot Card Booth. three: Get funnel cake. or four: Quit game. Type the option you are selecting in lowercase with no spaces or colons please! Currently, you have {points} points! ")
        if path == "one":
            ferris_wheel()
        else:
            if path == "two":
                tarot()
            else:
                if path == "three":
                    points = points + funnel_cake(int(points))
                else:
                    if path == "four":
                        print(f"Goodbye {player}! Thank you so much for playing! You earned {points} points! Amazing job!")


if __name__ == "__main__":
    main()

# I received the tarot card information from https://www.tarotparlor.com/blog/most-positive-tarot-cards