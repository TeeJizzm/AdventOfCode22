import os

from tools import texttolists as tl
from tools import rockpaperscissors as rps

############################

points = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "X" : 1,
    "Y" : 2,
    "Z" : 3
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

    playerPoints = sum(points[player] + rpsMatrix[points[player]-1][points[opponent]-1] for opponent, player in rounds)
    opponentPoints = sum(points[player] + (6 - rpsMatrix[points[player]-1][points[opponent]-1]) for opponent, player in rounds)

    opponentScore, playerScore, playerScore2 = 0, 0, 0

    roundScore = []

    for opponent,player in rounds:
        
        roundScore.append(points[player] + rpsMatrix[points[opponent]-1][points[player]-1])


        pointsOpp, pointsPla = points[opponent], points[player]

        #print("Played: ", pointsOpp, " ", pointsPla)

        scorePla = rpsMatrix[pointsOpp-1][pointsPla-1]
        scoreOpp = 6 - scorePla

        roundPla = pointsPla + scorePla
        roundOpp = pointsOpp + scoreOpp

        playerScore2 += roundPla
        opponentScore += roundOpp

    playerScore = sum(roundScore)

    print("Short calc= ", playerScore)

    print("Long Calc = ", playerScore2)

    print("One liner = ", playerPoints)

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