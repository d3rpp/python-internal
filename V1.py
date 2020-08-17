# Hudson Curren - 2.7 Internal Assesment
# Version 1
# Initializing pretty much everything

# allows printing the loading icon
import sys

# allows the clear function
from os import name, system

# allows intentional delays
from time import sleep

# allows threading so the program can animate loading AND process data
# unlike most microsoft apps.
import threading

# allows saving to JSON file. along with importing  
import json

#region GLOBALS
# Splash screen, always at the top, unless quitting application.
SPLASH:str = \
"""
BikeOS v0.0.1 (c) Hudson Curren - 2020
"""


#endregion

#region UTILITY FUNCTIONS

# clears the screen
def clear(printSplash:bool) -> bool:
    try:
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

        if printSplash:
            print(SPLASH)

        return True
    except e:
        return False

# animates loading spinner
def createLoadingSpinner(message:str) -> None:
    icon : [str] = ["|", "\\", "-", "/"]
    for i in icon:
        sys.stdout.write(f"{message}: {i}")
        sys.stdout.flush()
        sleep(0.2)

#endregion

#region PLAYER CLASS
class Player:
    """
        stores a name and score array.
        has a bunch of functions.
    """

    name:str
    scores:[int]

    def __init__(self, name:str):
        self.name = name

    def getScores(self) -> [int]:
        return self.scores
    
    def getScoresSum(self) -> int:
        tmp:int = 0
        for i in self._scores:
            tmp += i
        return tmp

    # use RACE NUMBER NOT ARRAY INDEX
    def addScore(self, index:int, score:int) -> bool:
        """
        USE RACE NUMBER NOT ARRAY INDEX
        """
        try:
            self.scores.insert(index - 1, score)
            return True
        except IndexError:
            print("I SAID USE RACE NUMBER")
            return False
        except ...:
            return False
#endregion

#region TEAM CLASS
class Team:
    """
        Stores an array of players, allong with collecively accessing their buitlin functions.

        also has a team name :D
    """

    teamName:str
    players:[Player]

    def __init__(self, _players:[Player], _teamName:str=""):
        self.teamName  = _teamName
        self.players = _players


#endregion

# funny big words :D
#   __  __           _             ______                          _     _                 
#  |  \/  |         (_)           |  ____|                        | |   (_)                
#  | \  / |   __ _   _   _ __     | |__     _   _   _ __     ___  | |_   _    ___    _ __  
#  | |\/| |  / _` | | | | '_ \    |  __|   | | | | | '_ \   / __| | __| | |  / _ \  | '_ \ 
#  | |  | | | (_| | | | | | | |   | |      | |_| | | | | | | (__  | |_  | | | (_) | | | | |
#  |_|  |_|  \__,_| |_| |_| |_|   |_|       \__,_| |_| |_|  \___|  \__| |_|  \___/  |_| |_|
def main():
    pass


main()