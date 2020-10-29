
# Hudson Curren - 2.7 Internal Assesment
# Version 9

# TODO: Not Accepting "" for placing
# TODO: ON FINAL PLACING, PROGRAM CRASHES
# TODO: PLACE FUNCTION COMMENTS UNDER DEFINITION
# TODO: Add Commenting
# TODO: "Calculations showing tally"

# TEXT GENERATOR: https://fsymbols.com/generators/blocky/

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
# import json

# TABULATE
# Copyright (c) 2011-2020 Sergey Astanin and contributors

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
import tabulate

from random import randint
#region GLOBALS
# Splash screen, always at the top, unless quitting application.
SPLASH:str = \
"""\
BikeOS v0.0.1 (c) Hudson Curren - 2020
"""
#endregion

#region UTILITY FUNCTIONS

# clears the screen
def clear(printSplash:bool = True) -> None:
    """clears the console/terminal

    Args:
        printSplash (bool): wheather or not to print the splash screen
    """
    try:
        if name == 'nt':
            _ = system('cls')
            pass
        else:
            _ = system('clear')
            pass

        if printSplash:
            print(SPLASH)
    except:
        pass

# animates loading spinner
def createLoadingSpinner(message:str, clearWithSplash:bool=True) -> None:
    """
    makes a loading bar. should be don synchronously whilst the actual task is done on seperate thread.

    Args:
        message (str): What to Display e.g. (Loading /)
    """
    icon : [str] = ["|", "\\", "-", "/"]
    print(message, end=" ")
    for i in icon:
        sys.stdout.write(i)
        sys.stdout.flush()
        sleep(0.1)
        sys.stdout.write('\b')
    clear(clearWithSplash)

def getIntegerInput(question:str = "") -> int:
    """Get an integer input from the user

    Args:
        question (str): the question to ask the user

    Returns:
        int: the integer they typed.
    """
    while True:
        try:
            clear(False)
            tmp = int(input(question))
            if tmp == "":
                return 0
            elif tmp < 1:
                raise ValueError
            return tmp
        except ValueError:
            print("Sorry, but that is not a valid number. please use the digits (0 - 9)")
            sleep(1)
            input()
            continue

def getStringInput(question:str = "") -> str:
    """Gets input from user

    Args:
        question (str): The question for the user

    Returns:
        str: whatever the user just typed
    """
    while True:
        tmp = str(input(question))
        if tmp == "":
            clear()
            print("Sorry, that string is empty")
        else:
            return tmp

def getYesOrNo(question:str = "") -> bool:
    while True:
        clear()
        a:str = input(f"{question} (Y/N) ")
        try:
            if a[0] == 'y' or a[0] == 'Y':
                return True
            elif a[0] == 'n' or a[0] == 'N':
                return False
            else:
                print("Please type either \"Y\" for yes or \"N\" for no")
        except IndexError:
            print("Please type either \"Y\" for yes or \"N\" for no")

#endregion

#region PLAYER CLASS
class Rider:
    riderName:str
    scores:[int]
    teamName:str

    def __init__(self, name:str = "NONAME", teamName:str = "NOTEAM"):
        self.riderName:str = name
        self.scores:[int] = []
        self.teamName:str = teamName

    def getScores(self) -> [int]:
        return self.scores
    
    def getScoreSum(self) -> int:
        tmp:int = 0
        for i in self.scores:
            tmp += i
        return tmp

    def getName(self) -> str:
        return self.riderName

    def getTeamName(self) -> str:
        return self.teamName

    def addScore(self, score:int) -> None:
        self.scores.append(score)
            
        
#endregion

#region TEAM CLASS
class Team:
    """
        Stores an array of players, allong with collecively accessing their buitlin functions.

        also has a team name :D
    """

    teamName:str
    rider:[Rider]

    def __init__(self, _players:[Rider], _teamName:str=""):
        self.teamName  = _teamName
        self.rider = _players
    
    def getTeamScoreSum(self):
        tmp:int = 0
        for i in self.rider:
            tmp += i.getScoreSum()

#endregion

#region RACE CLASS
class Race:
    """
    Contains a lot of stuff
    just in the form of a lot of instances of classes
    """
    raceName:str
    teams:[Team]

    def __init__(self):
        self.teams = []

    def SortTeamsByScores(self) -> [Team]:
        sortTeamsInRace(self.teams)

    def insertTeam(self, team:Team) -> None:
        self.teams.append(team)

#endregion

#region Sorting Algorithms
def sortPlayersInTeam(riders:[Rider]) -> [Rider]:
    n:int = len(riders)
    # using copy otherwise python automatically passes a reference, 
    # meaning we directly edit the object
    tmp:[Rider] = riders.copy()
    # for each element in array
    for i in range(n-1):
        # previous element are already in place
        for j in range(0,n-i-1):
            # if the score is greater at tmp[j] is greater than tmp[j+1],
            # swap them
            if (tmp[j].getScoreSum() < tmp[j+1].getScoreSum()):
                print(f'[Swap Sort] {tmp[j].getScoreSum()} < {tmp[j+1].getScoreSum()} --- Switching')
                sleep(0.1)
                clear()
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
            else:
                print(f'[Swap Sort] {tmp[j].getScoreSum()} > {tmp[j+1].getScoreSum()} --- Not Switching')
                sleep(0.1)
                clear()
    return tmp

# this is far from memory efficient and will not scale well

def sortTeamsInRace(teams:[Team]) -> [Team]:
    n:int = len(teams)
    tmp: [Team] = teams.copy()

    for i in range(n-1):
        for j in range(0,n-i-1):
            if (tmp[j].getTeamScoreSum() < tmp[j+1].getTeamScoreSum()):
                print(f'[Swap Sort] {tmp[j].getTeamScoreSum()} < {tmp[j+1].getTeamScoreSum()} --- Switching')
                sleep(0.25)
                clear()
                tmp[j], tmp[j+1] = tmp[j+1], tmp[j]
            else:
                print(f'[Swap Sort] {tmp[j].getTeamScoreSum()} < {tmp[j+1].getTeamScoreSum()} --- Switching')
                sleep(0.25)
                clear()
    return tmp

#endregion

#region CRASH FUNCTION
def CRASH(code):
    sys.exit(code)
#endregion

#region INIT
# GLOBAL RACE VARIABLE
RACE:Race = Race()


# ██╗███╗░░██╗██╗████████╗  ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
# ██║████╗░██║██║╚══██╔══╝  ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
# ██║██╔██╗██║██║░░░██║░░░  █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
# ██║██║╚████║██║░░░██║░░░  ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
# ██║██║░╚███║██║░░░██║░░░  ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
# ╚═╝╚═╝░░╚══╝╚═╝░░░╚═╝░░░  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

def INIT():

    # INIT RACE
    clear()
    raceNameTMP = getStringInput("What is this race called? ")
    RACE.raceName = raceNameTMP
    clear()
    print(f"Nice! lets get teams setup for {raceNameTMP}")
    sleep(2)
    del raceNameTMP

    i:int = 1
    # Init Teams
    while True:
        teamName: str
        print(f"What is team {i} being called?")
        print(f"try something like \"Fast Awesome Racing Team\"")
        teamName = getStringInput()

        j:int = 1 
        TMPPlayers: [Rider] = []
        while True:
            clear()
            print(f"\nWhat is the name of Racer {j} in {teamName}")
            TMPName = getStringInput()
            TMPPlayers.append(Rider(TMPName, teamName))
            if not getYesOrNo(f"Is there another Racer on team {teamName}?"):
                break
            else:
                j+=1
        
        RACE.insertTeam(Team(TMPPlayers, teamName))

        if not getYesOrNo("Is there another Team in this race?"):
            break
        else:
            i+=1


#endregion

#region MAINLOOP
#TODO: IMPLEMENT MAINLOOP FUNCTIONALITY
# 'tis a chonky boi
def mainLoop() -> None:
    input("Hit [Return] to begin")
    clear(False)
    print(f"Starting Race in")
    sleep(1)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    clear(False)
    print("""
  ____  ___  _
 / ___|/ _ \\| |
| |  _| | | | |
| |_| | |_| |_|
 \\____|\\___/(_)

    """)

# trust me, the GO! may look ugly but the extra backslashes are necessary

    t = threading.Thread(target=bootsqnc)
    t.start()

    while True:
        if t.is_alive():
            createLoadingSpinner("Racing", False)
        else:
            t.join()
            break
    
    del t

    # dont judge me for using threads
    # please

    print('Ready to Receive input')
    sleep(2)

    for i in RACE.teams.copy():
        for j in i.players.copy():
            # i = Team
            # j = Player in team

            # BUG: This refuses to get the name of j
            name:str = j.getName()
            team:str = j.getTeamName()
            q:str = (f'What was the final place for {name}, ({team})\nIf they didn\'t compete, just leave this blank\n> ')
            ans:int = getIntegerInput(q)
            tmp:int
            if ans == 1:
                tmp = 5
            elif ans == 2:
                tmp = 3
            elif ans == 3:
                tmp = 1
            else:
                tmp = 0
            j.addScore(tmp)

#endregion


#region PRINT
def printFinalOutput() -> None:
    fullTeamList = RACE.SortTeamsByScores()

    fullPlayerList:[Rider] = []
    for i in fullTeamList:
        for j in i.players:
            fullPlayerList.append(j)

    fullPlayerListSORTED:[Rider] =  sortPlayersInTeam(fullPlayerList)

    fullPlayerListSORTED_FOR_PRINTING = [["Place","Name", "Team", "Score"]]

    for i in range(len(fullPlayerListSORTED)):
        fullPlayerListSORTED_FOR_PRINTING.append([i+1,fullPlayerListSORTED[i].getName(), fullPlayerListSORTED[i].getTeamName(), fullPlayerListSORTED[i].getScoreSum()])

    tablified = tabulate(fullPlayerListSORTED_FOR_PRINTING, headers="firstrow")
    clear(True)
    print("\n\n")
    print(tablified)


    
#endregion

# funny big words :D

# ███╗░░░███╗░█████╗░██╗███╗░░██╗  ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗
# ████╗░████║██╔══██╗██║████╗░██║  ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
# ██╔████╔██║███████║██║██╔██╗██║  █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║
# ██║╚██╔╝██║██╔══██║██║██║╚████║  ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║
# ██║░╚═╝░██║██║░░██║██║██║░╚███║  ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║
# ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝  ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝

#region IGNORE THIS
def bootsqnc() -> None:
    sleep(3)
# move along

#endrgion

def main() -> int:
    
    # Loading Screen AMIRITE
    t = threading.Thread(target=bootsqnc)
    t.start()

    while True:
        if t.is_alive():
            createLoadingSpinner("Starting up Please Wait")
        else:
            clear()
            t.join()
            break
    
    del t

    INIT()

    # i for iteration
    i:int = 1

    while True:
        mainLoop()
        printFinalOutput()
        input()
        if getYesOrNo("are these teams racing again?\n"):
            continue
        else:
            break
    

    # TODO: PRINT OUTPUT

    clear(False)
    
    return 0

# EXITS THE PROGRAM WITH A SPECIFIED CODE
if __name__ == "__main__":
    sys.exit(main())

# main functions commented out for now, to test algorithms
# if im being honest, adding the return 0 to the main function gives this more of a c++ kinda vibe
# it makes me feel more comfortable doing this.
# it also means i can specify an exit code, should something go to sh*t

# TESTING SECTION
# lmao:[Player] = []
# lmao.append(Player(str('1'), 1))
# lmao.append(Player(str('2'), 1))
# lmao.append(Player(str('3'), 1))
# lmao.append(Player(str('4'), 1))
# lmao.append(Player(str('5'), 1))
# lmao.append(Player(str('6'), 1))

# for i in range(len(lmao)):
#     lmao[i].scores=([randint(0,5)]*3)

# lmao2 = sortPlayersInTeam(lmao).copy()

# tab:[] = [["Name", "Score"]]

# for i in lmao2:
#     tab.append([i.playerName, i.getScoreSum()])

# # TABULATE YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEAH
# tab2 =tabulate(tab, headers="firstrow") 

# # tab2 is now a very long string :D
# print(tab2)
