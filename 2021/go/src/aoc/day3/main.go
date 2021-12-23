package main

import (
	"aoc/common"
	"fmt"
	"strconv"
	"strings"
)

func main() {

	data := common.FileToByteArray("input.txt")
	binaryNumberList := strings.Fields(string(data))

	// Part 1
	// O(n * m)
	// n = 1000, m = 12

	sums := [12]int{}

	for i := 0; i < len(sums); i++ {
		sums[i] = sumOnes(binaryNumberList, i)
	}

	var gamma strings.Builder
	var epsilon strings.Builder
	for i := 0; i < len(sums); i++ {
		if sums[i] > len(binaryNumberList)/2 {
			gamma.WriteRune('1')
			epsilon.WriteRune('0')
		} else {
			gamma.WriteRune('0')
			epsilon.WriteRune('1')
		}
	}

	gammaResult := common.BinaryToDecimal(gamma.String())
	epsilonResult := common.BinaryToDecimal(epsilon.String())
	ans := gammaResult * epsilonResult

	fmt.Println("Part 1: ", ans)

	// Part 2

	sums = [12]int{}

	var o2GenRating string
	var co2ScrubberRating string
	o2Input := binaryNumberList
	co2Input := binaryNumberList
	for i := 0; i < len(sums); i++ {

		o2OnesCount := sumOnes(o2Input, i)
		co2OnesCount := sumOnes(co2Input, i)

		var mostOf string
		if (len(o2Input) - o2OnesCount) > o2OnesCount {
			mostOf = "0"
		} else {
			mostOf = "1"
		}

		var leastOf string
		if (len(co2Input) - co2OnesCount) > co2OnesCount {
			leastOf = "1"
		} else {
			leastOf = "0"
		}

		o2Filter := func(s string) bool { return string(s[i]) == mostOf }
		co2Filter := func(s string) bool { return string(s[i]) == leastOf }

		o2Input = common.Filter(o2Input, o2Filter)
		co2Input = common.Filter(co2Input, co2Filter)

		if len(o2Input) == 1 {
			o2GenRating = o2Input[0]
		}

		if len(co2Input) == 1 {
			co2ScrubberRating = co2Input[0]
		}
	}

	o2Dec := common.BinaryToDecimal(o2GenRating)
	co2Dec := common.BinaryToDecimal(co2ScrubberRating)
	ans = (o2Dec * co2Dec)

	fmt.Println("Part 2: ", ans)

}

func sumOnes(array []string, position int) (sum int) {
	for _, s := range array {
		str := []rune(s)
		val, _ := strconv.Atoi(string(str[position]))
		sum += val
	}

	return
}
