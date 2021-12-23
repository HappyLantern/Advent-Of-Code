package main

import (
	"aoc/common"
	"fmt"
	"strconv"
	"strings"
)

type Point struct {
	x int
	y int
}

func main() {

	data := common.FileToByteArray("input.txt")
	strData := strings.Split(string(data), "\n")

	ventMap := make(map[Point]int)

	for _, str := range strData {

		from, to := getFromAndTo(str)

		var points []Point

		temp := from
		if from.x < to.x {
			from = to
			to = temp
		}

		if from.x == to.x || from.y == to.y {
			fmt.Println("Straight: ", from, to)
			points = findStraightLineSegment(from, to)
		} else {
			fmt.Println("Diagonal: ", from, to)
			points = findDiagonalLineSegment(from, to)
		}

		fmt.Println("Points: ", points)

		for _, point := range points {
			ventMap[point] += 1
		}
	}

	values := make([]int, 0, len(ventMap))

	for _, v := range ventMap {
		if v >= 2 {
			values = append(values, v)
		}
	}

	fmt.Println(len(values))
}

func getFromAndTo(input string) (Point, Point) {

	toAndFrom := strings.Split(input, "->")

	if len(toAndFrom) != 2 {
		panic("Something went wrong")
	}

	return pointFromString(toAndFrom[0]), pointFromString(toAndFrom[1])
}

func findStraightLineSegment(from Point, to Point) (res []Point) {
	if from.x == to.x {
		for y := from.y; y <= to.y; y++ {
			point := Point{x: from.x, y: y}
			fmt.Println("POINT:", point)
			res = append(res, point)
		}
	} else {
		for x := from.x; x <= to.x; x++ {
			point := Point{x: x, y: from.y}
			fmt.Println("POINT:", point)
			res = append(res, point)
		}
	}

	return
}

func findDiagonalLineSegment(from Point, to Point) (res []Point) {
	var sign int

	if from.y > to.y {
		sign = -1
	} else {
		sign = 1
	}

	diff := 0
	y := from.y
	for x := from.x; x <= to.x; x++ {
		point := Point{x: x, y: y}
		res = append(res, point)
		diff += 1
		y += sign * diff
	}

	return
}

func pointFromString(input string) Point {
	xy := strings.Split(input, ",")

	x_int, _ := strconv.Atoi(strings.TrimSpace(xy[0]))
	y_int, _ := strconv.Atoi(strings.TrimSpace(xy[1]))

	return Point{x: x_int, y: y_int}
}
