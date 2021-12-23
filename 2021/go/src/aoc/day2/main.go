package main

import (
	"aoc/common"
	"fmt"
	"strconv"
	"strings"
)

func main() {

	data := common.FileToByteArray("input.txt")
	moves := strings.Split(string(data), "\n")
	hSum := 0
	dSum := 0

	// Part 1
	for i := 0; i < len(moves); i++ {
		move := strings.Fields(moves[i])

		a, err := strconv.Atoi(move[1])
		if err != nil {
			panic(err)
		}

		if move[0] == "forward" {
			hSum += a
		}
		if move[0] == "down" {
			dSum += a
		}
		if move[0] == "up" {
			dSum -= a
		}
	}

	ans := hSum * dSum

	fmt.Println("Part 1:", ans)

	// Part 2

	hSum = 0
	dSum = 0
	aSum := 0

	for i := 0; i < len(moves); i++ {
		move := strings.Fields(moves[i])

		a, err := strconv.Atoi(move[1])
		if err != nil {
			panic(err)
		}

		if move[0] == "forward" {
			hSum += a
			dSum += aSum * a
		}
		if move[0] == "down" {
			aSum += a
		}
		if move[0] == "up" {
			aSum -= a
		}
	}

	ans = hSum * dSum

	fmt.Println("Part 2:", ans)
}
