package common

import (
	"strconv"
	"strings"
)

func Filter(ss []string, test func(string) bool) (ret []string) {
	for _, s := range ss {
		if test(s) {
			ret = append(ret, s)
		}
	}
	return
}

func BinaryToDecimal(s string) int64 {
	res, err := strconv.ParseInt(s, 2, 64)

	if err != nil {
		panic(err)
	}

	return res
}

func StringArrayToIntArray(s []string) (res []int) {
	for _, str := range s {
		val, err := strconv.Atoi(strings.Trim(str, "\r"))

		if err != nil {
			panic(err)
		}

		res = append(res, val)
	}

	return res
}
