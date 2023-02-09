/* ################################## ##
#### ### ### Advent of Code ### ### ####
# www.github.com/TeeJizzm/AdventOfCode #
## ################################## */

// Day 01

// -----------------------------------

package main

// Imports
import (
	// Input/Output
	"fmt"
	"io/ioutil"

	// String manipulation
	"strconv"
	"strings"

	// Day specific
	"sort"
)

/* -----------------------------------
// Functions */

func main() {
	fmt.Println("Day 01 - Calorie Counting")

	// ------------ File -------------

	//*/ - File switch
	file, err := ioutil.ReadFile("day01/inc/ex.txt")
	/*/ //
	file, err := ioutil.ReadFile("day01/inc/in.txt")
	// --- End --- */

	if err != nil {
		fmt.Println(err)
	}

	// Added fix for Windows newline
	text := strings.ReplaceAll(string(file), "\r\n", "\n")
	//fmt.Print(text)

	// ----------- Setup -------------

	elves := strings.Split(text, "\n\n")

	cals := make([]int, len(elves))

	for j, elf := range elves {
		cals[j] = 0

		items := strings.Fields(elf)

		for _, cal := range items {
			if cal != "" {

			}
			i, err := strconv.Atoi(cal)
			if err != nil {
				panic(err)
			}
			cals[j] += i
		}
	}

	//fmt.Println(cals)

	// ----------- Output ------------

	fmt.Println("Part 1:", sumTop(cals, 1))
	fmt.Println("Part 2:", sumTop(cals, 3))

} // End main

// -----------------------------------

func sumTop(array []int, num int) int {
	srt := array[:]
	sort.Ints(srt)
	total := 0

	for i := 1; i <= num; i++ {
		total += srt[len(srt)-i]
	}
	return total
}
