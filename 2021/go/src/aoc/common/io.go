package common

import (
	"io/ioutil"
	"log"
)

// oh my
func FileToByteArray(path string) []byte {

	body, err := ioutil.ReadFile(path)

	if err != nil {
		log.Fatalf("unable to read file: %v", err)
	}

	return body
}

func filter(ss []string, test func(string) bool) (ret []string) {
	for _, s := range ss {
		if test(s) {
			ret = append(ret, s)
		}
	}
	return
}
