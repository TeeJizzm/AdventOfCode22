/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 02

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"io/ioutil"

	// String manipulation
	"strings"
	//"strconv"
	// Other required imports
)

/* -----------------------------------
// Functions */

func main() {
	fmt.Println("Day 02 - Rock Paper Scissors")

	// ------------ File -------------

	/*// - File switch
	file, err := ioutil.ReadFile("day02/inc/ex.txt")
	/*/
	file, err := ioutil.ReadFile("day02/inc/in.txt")
	// --- End --- */

	if err != nil {
		fmt.Println(err)
	}

	// Added fix for Windows newline
	text := strings.ReplaceAll(string(file), "\r\n", "\n")
	//fmt.Println(text)

	// ----------- Setup -------------

	rounds := strings.Split(text, "\n")

	var part1 uint = 0
	var part2 uint = 0

	matrix := map[string]uint8{"A": 1, "B": 2, "C": 3,
		"X": 1, "Y": 2, "Z": 3}

	var part1_mat = map[uint8]map[uint8]uint8{
		1: {1: 4, 2: 8, 3: 3},
		2: {1: 1, 2: 5, 3: 9},
		3: {1: 7, 2: 2, 3: 6}}

	var part2_mat = map[uint8]map[uint8]uint8{
		1: {1: 3, 2: 4, 3: 8},
		2: {1: 1, 2: 5, 3: 9},
		3: {1: 2, 2: 6, 3: 7}}

	// ----------- Output ------------

	for _, round := range rounds {
		plays := strings.Split(round, " ")

		part1 += uint(part1_mat[matrix[plays[0]]][matrix[plays[1]]])

		part2 += uint(part2_mat[matrix[plays[0]]][matrix[plays[1]]])

	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

// -----------------------------------
