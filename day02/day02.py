import os

import tools.texttolists as tl

############################

decode = {
    "A" : 1, # Rock
    "B" : 2, # Paper
    "C" : 3, # Scissors
    "X" : 1, # Rock
    "Y" : 2, # Paper
    "Z" : 3  # Scissors
    }

scoreMatrix = [
    [3,0,6], # 6 points for a win,
    [6,3,0], # 3 points for a tie,
    [0,6,3]  # 0 points for a loss
]  

responseMatrix = [
    [3,1,2], # 1 for rock
    [1,2,3], # 2 for paper
    [2,3,1]  # 3 for scissors
]

############################

def day2(rounds):
    print("Day 2 - Rock, Paper, Scissors")

    rounds = tl.toLists(filepath, "\n", " ")

    ## Part 1
    roundScores = [decode[player] + scoreMatrix[decode[player]-1][decode[opponent]-1] for  opponent, player in rounds]
    #roundScoresOpp = [played[opponent] + rpsMatrix[played[opponent]-1][played[player]-1] for  opponent, player in rounds]

    print("Part 1: ", sum(roundScores))

    ## Part 2
    score = {1:0, 2:3, 3:6}

    newScores = [score[decode[player]] + responseMatrix[decode[player]-1][decode[opponent]-1] for opponent, player in rounds]

    print("Part 2: ", sum(newScores))

############################

# Run script with chosen file

if __name__ == "__main__":
    # Change file
    #######
    day = "day02" 
    file = "input1.txt"
    #######
    
    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day2(filepath)

    
########### EOF ############