import os

import tools.texttolists as tl

############################

# Returns true/false for if a given string repeats
def hasRepeats(string):
    if len(set(string)) < len(string): return True
    else: return False

# Gives the index of the first unique string sequence
# String and part length are defined
def findRepeats(message, length=4):
    for i in range(0, len(message) - length + 1):
        if not hasRepeats(message[i:i+length]):
            return (i+length)
    return -1 # Return index = -1 if no unique sequence


def day06(filepath):
    print("Day 6 - Tuning Trouble")

    messages = tl.toLists(filepath)

    for message in messages:
        print(message[0])
        startOfPacket = findRepeats(message[0], 4)
        startOfMessage = findRepeats(message[0], 14)

        print(startOfPacket)
        print(startOfMessage)


############################

if __name__ == "__main__":
    # Change file
    #######
    day = "day06"
    file = "input.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day06(filepath)
    
########### EOF ############