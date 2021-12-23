package main

import (
	"aoc/common"
	"fmt"
	"strconv"
	"strings"
)

func main() {

	data := common.FileToByteArray("input.txt")

	// Part 1
	strData := strings.Fields(string(data))
	ans := 0
	for i := 1; i < len(strData); i++ {
		if (strData[i-1]) < (strData[i]) {
			ans += 1
		}
	}
	fmt.Println("Part 1: ", ans)

	// Part 2
	intData := []int{}

	for _, i := range strData {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}
		intData = append(intData, j)
	}

	ans = 0
	for i := 1; i < len(intData)-2; i++ {

		A := intData[i-1] + intData[i] + intData[i+1]
		B := intData[i] + intData[i+1] + intData[i+2]

		if A < B {
			ans += 1
		}
	}
	fmt.Println("Part 2: ", ans)

}
