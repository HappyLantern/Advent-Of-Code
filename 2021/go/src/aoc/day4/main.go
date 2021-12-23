package main

import (
	"aoc/common"
	"fmt"
	"strings"
)

type Board struct {
	Values  [][]int
	Checked [][]bool
	size    int
	bingo   bool
}

func main() {
	data := common.FileToByteArray("input.txt")
	strData := strings.Split(string(data), "\n")

	numbers := strings.Split(strData[0], ",")
	numbersInt := common.StringArrayToIntArray(numbers)

	boards := []Board{}
	for i := 2; i < len(strData); i += 6 {
		boards = append(boards, createBoard(strData[i:i+5]))
	}

	var winningBoard Board
	var winningNumber int

	// Part 1
out:
	for _, number := range numbersInt {

		for _, board := range boards {
			board = play(board, number)
			board = checkBingo(board)

			if board.bingo {
				winningBoard = board
				winningNumber = number
				break out
			}
		}
	}

	ans := winningNumber * sumOfUnmarked(winningBoard)
	fmt.Println("Part 1: ", ans)

	// Part 2

	// Reset boards
	boards = []Board{}
	for i := 2; i < len(strData); i += 6 {
		boards = append(boards, createBoard(strData[i:i+5]))
	}

	var lastWinningBoard Board
	var lastWinningNumber int
out2:
	for _, number := range numbersInt {

		for idx, board := range boards {

			board = play(board, number)
			board = checkBingo(board)

			boards[idx] = board // The bingo bool did not follow into the array, Appears u get a copy in the loop as well. The array values followed cuzz they have references to that data, I presume.

			allHaveBingo := true

			for _, board := range boards {
				if !board.bingo {
					allHaveBingo = false
				}
			}

			if allHaveBingo {
				lastWinningBoard = board
				lastWinningNumber = number
				break out2
			}
		}
	}

	ans = lastWinningNumber * sumOfUnmarked(lastWinningBoard)
	fmt.Println("Part 2: ", ans)
}

func checkBingo(board Board) Board {
	for i := 0; i < len(board.Checked); i++ {

		row := board.Checked[i]
		_, col := boardColumn(board, i)
		rowBingo := true
		colBingo := true

		for j := 0; j < len(row); j++ {
			if !row[j] {
				rowBingo = false
			}
		}

		for j := 0; j < len(col); j++ {
			if !col[j] {
				colBingo = false
			}
		}

		if rowBingo || colBingo {
			board.bingo = true
		}
	}

	return board
}

func play(board Board, number int) Board {
	for i := 0; i < board.size; i++ {
		row := board.Values[i]
		for j := 0; j < board.size; j++ {
			if row[j] == number {
				board.Checked[i][j] = true
			}
		}
	}

	return board
}

func createBoard(values []string) Board {
	boardValues := [][]int{}
	initChecked := [][]bool{{false, false, false, false, false}, {false, false, false, false, false}, {false, false, false, false, false}, {false, false, false, false, false}, {false, false, false, false, false}}

	for i := 0; i < len(values); i++ {
		temp := common.StringArrayToIntArray(strings.Fields(values[i]))
		boardValues = append(boardValues, temp)
	}

	return Board{Values: boardValues, Checked: initChecked, size: 5, bingo: false}
}

func boardColumn(board Board, columnIndex int) ([]int, []bool) {
	columnInt := make([]int, 0)
	columnBool := make([]bool, 0)

	for i := 0; i < board.size; i++ {
		rowVal := board.Values[i]
		rowChecked := board.Checked[i]

		columnInt = append(columnInt, rowVal[columnIndex])
		columnBool = append(columnBool, rowChecked[columnIndex])
	}

	return columnInt, columnBool
}

func sumOfUnmarked(board Board) (sum int) {
	for i := 0; i < board.size; i++ {

		rowValue := board.Values[i]
		rowChecked := board.Checked[i]

		for j := 0; j < board.size; j++ {
			if !rowChecked[j] {
				sum += rowValue[j]
			}
		}
	}

	return
}
