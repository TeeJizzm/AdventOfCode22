import os

from tools import texttolists as tl
from tools import rockpaperscissors as rps

############################

pointsPlayed = {
    "A" : 1, # Rock
    "B" : 2, # Paper
    "C" : 3, # Scissors
    "X" : 1, # Rock
    "Y" : 2, # Paper
    "Z" : 3  # Scissors
    }

rpsMatrix = [
        [3,0,6], # 6 points for a win,
        [6,3,0], # 3 points for a tie,
        [0,6,3]  # 0 points for a loss
        ]  

############################

def day2(filepath):
    print("Day 2 - Rock, Paper, Scissors")

    rounds = tl.toLists(filepath, "\n", " ")

    ## Part 1
    roundScores = [pointsPlayed[player] + rpsMatrix[pointsPlayed[player]-1][pointsPlayed[opponent]-1] for  opponent, player in rounds]
    #roundScoresOpp = [pointsPlayed[opponent] + rpsMatrix[pointsPlayed[opponent]-1][pointsPlayed[player]-1] for  opponent, player in rounds]

    print("Short calc= ", sum(roundScores), " len ", len(roundScores))

    ## Part 2


############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day02" 
    file = "input1.txt"
    #######
    
    # Get absolute filepath of file
    cwd = os.getcwd()
    filepath = os.path.join(cwd, day, file)
    
    day2(filepath)

    
########### EOF ############