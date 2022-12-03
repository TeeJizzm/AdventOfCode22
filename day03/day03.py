import os

with open("example.txt") as file:

    rucksacks = file.read().splitlines()

    for rucksack in rucksacks:

        partone = rucksack.split(len(rucksack) / 2)
