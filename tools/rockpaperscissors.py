# Tools for Rock Paper Scissors
# Calculates points for each player



############################

def playPoints(enc):

    if enc == "A" or enc == "X":
        return 1 # Rock, 1 point
    elif enc == "B" or enc == "Y":
        return 2 # Paper, 2 points
    elif enc == "C" or enc == "Z":
        return 3 # Scissors, 3 points


############################

# Calculate points scored in the round
# R=1, P=2, S=3; 
# Output player points

def scorePoints(player, opponent):

    # Weighted matrix with winning values
    rpsMatrix = [[3,0,6], # 6 points for a win,
                [6,3,0],  # 3 points for a tie,
                [0,6,3]]  # 0 points for a loss
    
    return rpsMatrix[opponent][player]

    # Calculate points for scoring

########### EOF ############