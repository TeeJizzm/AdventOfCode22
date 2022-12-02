import os

from tools import texttolists as tl
from tools import rockpaperscissors as rps

############################

def day2(filepath):
    print("Day 2 - Rock, Paper, Scissors")

    rounds = tl.toLists(filepath, "\n", " ")

    opponentScore, responseScore = 0, 0

    for round in rounds:
        
        resPlay = rps.playPoints(round[1])
        oppPlay = rps.playPoints(round[0])        

        resScore = rps.scorePoints(oppPlay, resPlay)
        oppScore = 6 - resScore

        responseScore += (resScore + resPlay)
        opponentScore += (oppScore + oppPlay)

        print(oppPlay)
        print(resPlay)

    print(responseScore)

############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day02" 
    file = "example1.txt"
    #######
    
    # Get absolute filepath of file
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    day2(filepath)

    
########### EOF ############