package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type Object struct {
	Depth int
	Prev  *Object
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	dat, err := ioutil.ReadFile("./input.txt")
	check(err)

	datArray := strings.Split(string(dat), "\n")
	datArray = datArray[:len(datArray)-1]

	objectMap := make(map[string]int)
	orbits := 0

	for _, element := range datArray {
		fmt.Println(element)
		objs := strings.Split(element, ")")
		center := objs[0]
		orbiter := objs[1]

		depth, ok := objectMap[center]
		if !ok {
			objectMap[center] = 0
			depth = 0
		}
		objectMap[orbiter] = depth + 1
		orbits += depth + 1
	}

	fmt.Println(orbits)
}
