import os

import tools.texttolists as tl

############################

def cargoCrane9000(columns, mv, frm, to):

    for moves in range(mv):
        columns[to-1].append(columns[frm-1].pop())

def cargoCrane9001(columns, mv, frm, to):

    columns[to-1].extend(columns[frm-1][-mv:])
    for moves in range(mv):
        columns[frm-1].pop()



def day05(filepath):
    print("Day 5 - Supply Stacks")

    # Read file
    crateIns, instructions = tl.toLists(filepath, "\n\n", "\n")
    
    ### Setup crates
    crateNums = crateIns.pop()
    crateIns.reverse()

    crates = []
    crates2 = []

    # Assign crates to variables
    for i in range(1, len(crateNums), 4):
        #print(crateNums[i])

        crate = []
        crate2 = []
        for j in range(len(crateIns)):
            if crateIns[j][i] != " ":
                crate.append(crateIns[j][i])
                crate2.append(crateIns[j][i])
    
        crates.append(crate) # Crates list finished
        crates2.append(crate2)
    
    print("a ", crates)
    print("b ", crates2)
    
    ### Decode instructions
    for instruction in instructions:
        _,mv,_,frm,_,to = instruction.split(" ")
        #print("Move ", mv, " from ", frm, " to ", to)
        cargoCrane9000(crates, int(mv), int(frm), int(to)) # perform movements
        #print("a ", crates)
        cargoCrane9001(crates2, int(mv), int(frm), int(to)) # perform movements
        print("b ", crates2)

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
    file = "input.txt"
    #######

    # Get absolute filepath of file
    filepath = os.path.join(os.getcwd(), day, file)
    
    day05(filepath)
    
########### EOF ############