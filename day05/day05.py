import os

import tools.texttolists as tl

############################

def cargoCrane9000(crates, mv, frm, to):
    print("Move ", mv, " from ", frm, " to ", to)

    for moves in range(mv):
        crates[to-1].append(crates[frm-1].pop())

def cargoCrane9001(crates, mv, frm, to):
    print("Move ", mv, " from ", frm, " to ", to) 

    temp = []
    for moves in range(mv):
        crates[to-1].append(crates[frm-1].pop())

    #crates[to-1].append(temp.reverse())



def day05(filepath):
    print("Day 5 - Supply Stacks")

    # Read file
    crateIns, instructions = tl.toLists(filepath, "\n\n", "\n")
    
    ### Setup crates
    crateNums = crateIns.pop()
    crateIns.reverse()

    crates = []

    # Assign crates to variables
    for i in range(1, len(crateNums), 4):
        #print(crateNums[i])

        crate = []
        for j in range(len(crateIns)):
            if crateIns[j][i] != " ":
                crate.append(crateIns[j][i])
    
        crates.append(crate) # Crates list finished
    
    crates2 = crates
    print(crates2)
    print(crates)
    
    ### Decode instructions
    for instruction in instructions:
        _,mv,_,frm,_,to = instruction.split(" ")
        cargoCrane9000(crates, int(mv), int(frm), int(to)) # perform movements
        cargoCrane9001(crates2, int(mv), int(frm), int(to))

        print(crates)
        print(crates2)

    ### Results
    part1, part2 = "", ""
    for i in range(len(crates)):
        part1 += str(crates[i][-1])
        part2 += str(crates2[i][-1])
    print("Part 1: ", part1)
    print("Part 2: ", part2)

############################

if __name__ == "__main__":
    # Change file
    #######
    day = "day05"
    file = "example.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day05(filepath)
    
########### EOF ############